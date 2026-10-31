"""
Validation and data quality checks for dataset.csv (academic prototype).
"""
from datetime import datetime
from typing import Dict, List, Any
from collections import Counter

from .load import REQUIRED_COLUMNS


TIMESTAMP_FMT = "%Y-%m-%d %H:%M:%S"


class DatasetValidationError(Exception):
    """Raised when dataset validation fails due to schema/format issues."""
    pass


def validate_rows(rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    report: Dict[str, Any] = {}
    n = len(rows)
    report["row_count"] = n
    if n == 0:
        report["errors"] = ["empty dataset"]
        raise DatasetValidationError("Dataset has no rows")

    # columns
    cols = list(rows[0].keys()) if rows else []
    report["columns"] = cols

    # Schema validation - required columns
    missing_cols = []
    for c in REQUIRED_COLUMNS:
        if c not in cols:
            missing_cols.append(c)
    if missing_cols:
        report["missing_required_columns"] = missing_cols
        report["errors"] = [f"missing_required_columns: {missing_cols}"]
        raise DatasetValidationError(f"Missing required columns: {missing_cols}")

    # missing values
    missing = Counter()
    for r in rows:
        for k, v in r.items():
            if v is None or str(v).strip() == "":
                missing[k] += 1
    report["missing"] = dict(missing)

    # duplicates (exact)
    seen = set()
    for r in rows:
        # use tuple of sorted items as key
        seen.add(tuple(sorted((k, str(v)) for k, v in r.items())))
    report["duplicate_rows"] = n - len(seen)

    # timestamp parse
    bad_ts = 0
    parsed_ts = []
    for i, r in enumerate(rows):
        ts = str(r.get("timestamp", "")).strip()
        try:
            dt = datetime.strptime(ts, TIMESTAMP_FMT)
            parsed_ts.append(dt)
        except Exception:
            bad_ts += 1
    report["timestamp_parse_errors"] = bad_ts
    report["timestamp_format_sample"] = [str(r.get("timestamp")) for r in rows[:3]]
    if parsed_ts:
        report["timestamp_min"] = parsed_ts[0].isoformat(sep=" ")
        report["timestamp_max"] = parsed_ts[-1].isoformat(sep=" ") if len(parsed_ts) == n and bad_ts == 0 else None
        # check sorted
        if len(parsed_ts) > 1:
            report["timestamps_sorted"] = all(parsed_ts[i] <= parsed_ts[i + 1] for i in range(len(parsed_ts) - 1))
        else:
            report["timestamps_sorted"] = True

    # numerics
    bad_trans = 0
    bad_score = 0
    trans_vals = []
    score_vals = []
    for r in rows:
        # trans_amount
        try:
            v = float(str(r.get("trans_amount")).strip())
            trans_vals.append(v)
        except Exception:
            bad_trans += 1
        # anomaly_score
        try:
            s = float(str(r.get("anomaly_score")).strip())
            score_vals.append(s)
        except Exception:
            bad_score += 1
    report["trans_amount_parse_errors"] = bad_trans
    report["anomaly_score_parse_errors"] = bad_score
    if trans_vals:
        report["trans_amount_min"] = min(trans_vals)
        report["trans_amount_max"] = max(trans_vals)
    if score_vals:
        report["anomaly_score_min"] = min(score_vals)
        report["anomaly_score_max"] = max(score_vals)
        report["anomaly_score_in_range_0_1"] = all(0.0 <= s <= 1.0 for s in score_vals)

    # is_anomaly
    bad_anom = 0
    anom_vals = []
    for r in rows:
        val = str(r.get("is_anomaly", "")).strip()
        if val not in ("0", "1"):
            bad_anom += 1
        else:
            anom_vals.append(int(val))
    report["is_anomaly_parse_errors"] = bad_anom
    report["is_anomaly_values_set"] = sorted(set(anom_vals)) if anom_vals else []
    report["is_anomaly_count_1"] = sum(1 for v in anom_vals if v == 1)
    report["is_anomaly_count_0"] = sum(1 for v in anom_vals if v == 0)
    if n > 0:
        report["is_anomaly_pct_1"] = round((report["is_anomaly_count_1"] / n) * 100, 4)

    # categories
    report["transaction_type_unique"] = sorted(set(str(r.get("transaction_type")).strip() for r in rows))
    report["merchant_category_unique"] = sorted(set(str(r.get("merchant_category")).strip() for r in rows))
    report["account_id_unique_count"] = len(set(str(r.get("account_id")).strip() for r in rows))

    report["errors"] = []
    if bad_ts > 0:
        report["errors"].append(f"timestamp_parse_errors={bad_ts}")
    if bad_trans > 0:
        report["errors"].append(f"trans_amount_parse_errors={bad_trans}")
    if bad_score > 0:
        report["errors"].append(f"anomaly_score_parse_errors={bad_score}")
    if bad_anom > 0:
        report["errors"].append(f"is_anomaly_parse_errors={bad_anom}")
    if missing:
        report["errors"].append(f"missing_values={dict(missing)}")

    if report["errors"]:
        # Collect all errors for clearer message
        err_msg = "; ".join(report["errors"])
        raise DatasetValidationError(f"Validation errors found: {err_msg}")

    return report
