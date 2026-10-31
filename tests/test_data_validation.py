import unittest
import os
import tempfile
import csv
from pathlib import Path

from src.data.load import load_dataset, DatasetLoadError
from src.data.validate import validate_rows, DatasetValidationError


class TestDataValidation(unittest.TestCase):
    def test_valid_dataset(self):
        rows = load_dataset("dataset.csv")
        report = validate_rows(rows)
        self.assertEqual(report["row_count"], 500)
        self.assertEqual(report["duplicate_rows"], 0)
        self.assertEqual(report["timestamp_parse_errors"], 0)
        self.assertEqual(report["trans_amount_parse_errors"], 0)
        self.assertEqual(report["anomaly_score_parse_errors"], 0)
        self.assertEqual(report["is_anomaly_parse_errors"], 0)
        self.assertEqual(report["errors"], [])

    def test_missing_file(self):
        with self.assertRaises(DatasetLoadError) as ctx:
            load_dataset("nonexistent_file_12345.csv")
        self.assertIn("File not found", str(ctx.exception))

    def test_empty_csv(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv", encoding="utf-8") as f:
            # write nothing
            fname = f.name
        try:
            with self.assertRaises(DatasetLoadError) as ctx:
                load_dataset(fname)
            self.assertIn("Empty file", str(ctx.exception))
        finally:
            os.unlink(fname)

    def test_header_only_csv(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "account_id", "trans_amount", "transaction_type", "merchant_category", "anomaly_score", "is_anomaly"])
            fname = f.name
        try:
            with self.assertRaises(DatasetLoadError) as ctx:
                load_dataset(fname)
            self.assertIn("no data rows", str(ctx.exception))
        finally:
            os.unlink(fname)

    def test_missing_required_column(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "account_id", "trans_amount", "transaction_type", "merchant_category", "anomaly_score"])  # missing is_anomaly
            writer.writerow(["2024-01-01 00:26:00", "ACC00001", "10.0", "Debit", "Online", "0.1"])
            fname = f.name
        try:
            rows = load_dataset(fname)
            with self.assertRaises(DatasetValidationError) as ctx:
                validate_rows(rows)
            self.assertIn("Missing required columns", str(ctx.exception))
        finally:
            os.unlink(fname)

    def test_invalid_timestamp(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "account_id", "trans_amount", "transaction_type", "merchant_category", "anomaly_score", "is_anomaly"])
            writer.writerow(["01/01/2024 00:26:00", "ACC00001", "10.0", "Debit", "Online", "0.1", "0"])
            fname = f.name
        try:
            rows = load_dataset(fname)
            with self.assertRaises(DatasetValidationError) as ctx:
                validate_rows(rows)
            self.assertIn("timestamp_parse_errors", str(ctx.exception))
        finally:
            os.unlink(fname)

    def test_non_numeric_trans_amount(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "account_id", "trans_amount", "transaction_type", "merchant_category", "anomaly_score", "is_anomaly"])
            writer.writerow(["2024-01-01 00:26:00", "ACC00001", "abc", "Debit", "Online", "0.1", "0"])
            fname = f.name
        try:
            rows = load_dataset(fname)
            with self.assertRaises(DatasetValidationError) as ctx:
                validate_rows(rows)
            self.assertIn("trans_amount_parse_errors", str(ctx.exception))
        finally:
            os.unlink(fname)

    def test_non_numeric_anomaly_score(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "account_id", "trans_amount", "transaction_type", "merchant_category", "anomaly_score", "is_anomaly"])
            writer.writerow(["2024-01-01 00:26:00", "ACC00001", "10.0", "Debit", "Online", "xyz", "0"])
            fname = f.name
        try:
            rows = load_dataset(fname)
            with self.assertRaises(DatasetValidationError) as ctx:
                validate_rows(rows)
            self.assertIn("anomaly_score_parse_errors", str(ctx.exception))
        finally:
            os.unlink(fname)

    def test_invalid_is_anomaly_value(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "account_id", "trans_amount", "transaction_type", "merchant_category", "anomaly_score", "is_anomaly"])
            writer.writerow(["2024-01-01 00:26:00", "ACC00001", "10.0", "Debit", "Online", "0.1", "true"])
            fname = f.name
        try:
            rows = load_dataset(fname)
            with self.assertRaises(DatasetValidationError) as ctx:
                validate_rows(rows)
            self.assertIn("is_anomaly_parse_errors", str(ctx.exception))
        finally:
            os.unlink(fname)

    def test_duplicate_rows(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "account_id", "trans_amount", "transaction_type", "merchant_category", "anomaly_score", "is_anomaly"])
            writer.writerow(["2024-01-01 00:26:00", "ACC00001", "10.0", "Debit", "Online", "0.1", "0"])
            writer.writerow(["2024-01-01 00:26:00", "ACC00001", "10.0", "Debit", "Online", "0.1", "0"])
            fname = f.name
        try:
            rows = load_dataset(fname)
            report = validate_rows(rows)
            self.assertEqual(report["duplicate_rows"], 1)
        finally:
            os.unlink(fname)


if __name__ == "__main__":
    unittest.main()
