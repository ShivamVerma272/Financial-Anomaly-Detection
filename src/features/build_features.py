"""
Feature engineering for Isolation Forest baseline.
Excludes is_anomaly and anomaly_score from model inputs.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from typing import Tuple, List, Dict, Any


CATEGORICAL_COLS = ["transaction_type", "merchant_category"]
EXCLUDE_COLS = ["is_anomaly", "anomaly_score"]


class FeatureEngineeringError(Exception):
    pass


def load_and_prepare(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = df.copy()
    report: Dict[str, Any] = {"rows": len(df)}
    # Parse timestamp
    if "timestamp" in df.columns:
        df["timestamp_parsed"] = pd.to_datetime(df["timestamp"], format="%Y-%m-%d %H:%M:%S", errors="coerce")
        report["timestamp_parse_failures"] = int(df["timestamp_parsed"].isna().sum())
    else:
        report["timestamp_parse_failures"] = len(df)
        df["timestamp_parsed"] = pd.NaT
    # Parse amounts
    if "trans_amount" in df.columns:
        df["trans_amount"] = pd.to_numeric(df["trans_amount"], errors="coerce")
        report["trans_amount_parse_failures"] = int(df["trans_amount"].isna().sum())
    else:
        report["trans_amount_parse_failures"] = len(df)
        df["trans_amount"] = np.nan
    # Parse anomaly_score if present (not used as input)
    if "anomaly_score" in df.columns:
        df["anomaly_score"] = pd.to_numeric(df["anomaly_score"], errors="coerce")
    # Parse is_anomaly if present (not used as input)
    if "is_anomaly" in df.columns:
        df["is_anomaly"] = pd.to_numeric(df["is_anomaly"], errors="coerce")
    return df, report


def build_features(df: pd.DataFrame, return_metadata: bool = False):
    df_prep, report = load_and_prepare(df)
    feat = df_prep.copy()

    # Create stable row identifier (original index)
    row_id = feat.index.copy()

    # Time features
    if "timestamp_parsed" in feat.columns and pd.api.types.is_datetime64_any_dtype(feat["timestamp_parsed"]):
        feat["hour"] = feat["timestamp_parsed"].dt.hour
        feat["dayofweek"] = feat["timestamp_parsed"].dt.day_of_week
        feat["day"] = feat["timestamp_parsed"].dt.day
        feat["month"] = feat["timestamp_parsed"].dt.month
        report["timestamp_derived_ok"] = int((~feat["timestamp_parsed"].isna()).sum())
    else:
        feat["hour"] = np.nan
        feat["dayofweek"] = np.nan
        feat["day"] = np.nan
        feat["month"] = np.nan
        report["timestamp_derived_ok"] = 0

    # Fill missing values
    if "trans_amount" in feat.columns and feat["trans_amount"].isna().sum() > 0:
        med = feat["trans_amount"].median()
        if pd.isna(med):
            raise FeatureEngineeringError("trans_amount cannot be parsed for any row")
        feat["trans_amount"] = feat["trans_amount"].fillna(med)
        report["trans_amount_filled_median"] = float(med)
    elif "trans_amount" not in feat.columns:
        feat["trans_amount"] = 0.0
    # Time features
    for c in ["hour", "dayofweek", "day", "month"]:
        if c not in feat.columns:
            feat[c] = 0
        if feat[c].isna().sum() > 0:
            if c == "hour":
                feat[c] = feat[c].fillna(0)
            elif c == "dayofweek":
                feat[c] = feat[c].fillna(0)
            elif c == "day":
                feat[c] = feat[c].fillna(1)
            elif c == "month":
                feat[c] = feat[c].fillna(1)
            report[f"{c}_filled"] = True

    # Check non-finite
    for c in ["trans_amount", "hour", "dayofweek", "day", "month"]:
        if c in feat.columns:
            feat[c] = feat[c].replace([np.inf, -np.inf], np.nan)
            feat[c] = feat[c].fillna(0.0)

    # One-hot encode categoricals
    cat_frames = []
    for c in CATEGORICAL_COLS:
        if c in feat.columns:
            dummies = pd.get_dummies(feat[c].astype(str), prefix=c)
            cat_frames.append(dummies)
    if cat_frames:
        feat = pd.concat([feat] + cat_frames, axis=1)

    # Build feature list excluding is_anomaly and anomaly_score and identifiers
    exclude = set(EXCLUDE_COLS)
    feature_cols = []
    for c in feat.columns:
        if c in exclude:
            continue
        if c in ["timestamp", "timestamp_parsed", "date"]:
            continue
        if c == "account_id":
            continue
        if pd.api.types.is_numeric_dtype(feat[c]) or feat[c].dtype == bool:
            feature_cols.append(c)
    if not feature_cols:
        for c in ["trans_amount", "hour", "dayofweek"]:
            if c in feat.columns and c not in exclude:
                feature_cols.append(c)
    X = feat[feature_cols].copy()
    for c in X.columns:
        if X[c].dtype == bool:
            X[c] = X[c].astype(int)
    X = X.fillna(0.0)
    # Final check
    if X.isna().sum().sum() > 0:
        raise FeatureEngineeringError("NaN values remain in features after processing")
    if not np.all(np.isfinite(X.values)):
        raise FeatureEngineeringError("Non-finite values remain in features")
    report["n_features"] = len(feature_cols)
    report["feature_cols"] = feature_cols
    if return_metadata:
        return X, feature_cols, row_id, report
    return X, feature_cols
