import unittest
import numpy as np
import pandas as pd

from src.features.build_features import build_features, FeatureEngineeringError
from src.models.baseline_iforest import IsolationForestBaseline
from src.evaluation.evaluate import exploratory_compare


class TestPhase2Review(unittest.TestCase):
    def test_feature_excludes_leakage(self):
        df = pd.DataFrame({
            "timestamp": ["2024-01-01 00:00:00"],
            "account_id": ["ACC001"],
            "trans_amount": ["10.0"],
            "transaction_type": ["Debit"],
            "merchant_category": ["Online"],
            "anomaly_score": ["0.5"],
            "is_anomaly": ["1"],
        })
        X, cols, row_id, report = build_features(df, return_metadata=True)
        self.assertNotIn("is_anomaly", X.columns)
        self.assertNotIn("anomaly_score", X.columns)
        self.assertNotIn("account_id", X.columns)
        self.assertNotIn("timestamp", X.columns)

    def test_malformed_timestamp_handling(self):
        df = pd.DataFrame({
            "timestamp": ["bad-date"],
            "account_id": ["ACC001"],
            "trans_amount": ["10.0"],
            "transaction_type": ["Debit"],
            "merchant_category": ["Online"],
            "anomaly_score": ["0.1"],
            "is_anomaly": ["0"],
        })
        X, cols, row_id, report = build_features(df, return_metadata=True)
        self.assertEqual(X.shape[0], 1)

    def test_missing_numeric_filled(self):
        df = pd.DataFrame({
            "timestamp": ["2024-01-01 00:00:00"],
            "account_id": ["ACC001"],
            "trans_amount": [np.nan],
            "transaction_type": ["Debit"],
            "merchant_category": ["Online"],
            "anomaly_score": ["0.1"],
            "is_anomaly": ["0"],
        })
        try:
            X, cols, row_id, report = build_features(df, return_metadata=True)
            self.assertFalse(X.isna().any().any())
        except FeatureEngineeringError:
            # If median can't be computed (all NaN) - acceptable to raise
            pass

    def test_invalid_contamination(self):
        with self.assertRaises(ValueError):
            IsolationForestBaseline(contamination=1.5)
        with self.assertRaises(ValueError):
            IsolationForestBaseline(contamination=-0.1)

    def test_empty_input(self):
        model = IsolationForestBaseline()
        with self.assertRaises(ValueError):
            model.fit_predict(pd.DataFrame())

    def test_one_row_input(self):
        X = pd.DataFrame({"f1": [1.0]})
        model = IsolationForestBaseline(contamination=0.1)
        res = model.fit_predict(X)
        self.assertEqual(len(res["flags"]), 1)

    def test_reproducibility(self):
        X = pd.DataFrame({"f1": [1.0, 2.0, 3.0], "f2": [0.1, 0.2, 0.3]})
        m1 = IsolationForestBaseline(contamination=0.33, random_state=123)
        m2 = IsolationForestBaseline(contamination=0.33, random_state=123)
        r1 = m1.fit_predict(X)
        r2 = m2.fit_predict(X)
        np.testing.assert_array_equal(r1["flags"], r2["flags"])

    def test_row_alignment(self):
        df = pd.DataFrame({
            "timestamp": ["2024-01-01 00:00:00", "2024-01-01 01:00:00"],
            "account_id": ["ACC001", "ACC002"],
            "trans_amount": ["10.0", "20.0"],
            "transaction_type": ["Debit", "Credit"],
            "merchant_category": ["Online", "Grocery"],
            "anomaly_score": ["0.1", "0.2"],
            "is_anomaly": ["0", "0"],
        })
        X, cols, row_id, report = build_features(df, return_metadata=True)
        model = IsolationForestBaseline(contamination=0.5)
        res = model.fit_predict(X)
        self.assertEqual(len(res["flags"]), len(row_id))
        self.assertTrue(all(row_id.values == df.index.values))

    def test_evaluation_warning(self):
        res = exploratory_compare(np.array([0,1]), np.array([0,0]))
        self.assertIn("EXPLORATORY", res["note"])
        self.assertIn("Do not claim", res["disclaimer"])


if __name__ == "__main__":
    unittest.main()
