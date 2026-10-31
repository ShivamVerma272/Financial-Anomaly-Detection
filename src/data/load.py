"""
Safe dataset loading utilities for the academic prototype.
"""
import csv
from pathlib import Path
from typing import Dict, List, Any


REQUIRED_COLUMNS = [
    "timestamp",
    "account_id",
    "trans_amount",
    "transaction_type",
    "merchant_category",
    "anomaly_score",
    "is_anomaly",
]


class DatasetLoadError(Exception):
    """Raised when dataset loading fails due to file/format issues."""
    pass


def load_dataset(path: str | Path) -> List[Dict[str, Any]]:
    path = Path(path)
    if not path.exists():
        raise DatasetLoadError(f"File not found: {path}")
    if not path.is_file():
        raise DatasetLoadError(f"Not a file: {path}")
    try:
        with path.open("r", encoding="utf-8") as f:
            content = f.read()
    except PermissionError as e:
        raise DatasetLoadError(f"Permission denied reading file: {path}") from e
    except OSError as e:
        raise DatasetLoadError(f"Unable to read file: {path} ({e})") from e

    if content.strip() == "":
        raise DatasetLoadError(f"Empty file: {path}")

    # Try to parse as CSV
    try:
        # Use StringIO to re-parse
        import io

        fobj = io.StringIO(content)
        reader = csv.DictReader(fobj)
        rows: List[Dict[str, Any]] = []
        for row in reader:
            rows.append(dict(row))
        if len(rows) == 0:
            # Could be header only
            raise DatasetLoadError(f"CSV contains no data rows (header only or malformed): {path}")
        return rows
    except DatasetLoadError:
        raise
    except csv.Error as e:
        raise DatasetLoadError(f"Malformed CSV in {path}: {e}") from e
    except Exception as e:
        raise DatasetLoadError(f"Failed to parse CSV {path}: {e}") from e


def get_required_columns() -> List[str]:
    return list(REQUIRED_COLUMNS)
