import unittest
import os
import tempfile
import numpy as np
import pandas as pd

from src.features.build_features import build_features, load_and_prepare
from src.models.baseline_iforest import IsolationForestBaseline
from src.evaluation.evaluate import exploratory_compare


class TestPhase2(unittest.TestCase):
    def setUp(self):
        # Create small test dataframe
        self.test_df = pd.DataFrame({
            "timestamp": ["2024-01-01 00:26:00", "2024-01-01 01:00:00", "2024-01-01 02:00:00"],
            "account_id": ["ACC001", "ACC002", "ACC001"],
            "trans_amount": ["10.5", "100.0", "20.0"],
            "transaction_type": ["Debit", "Credit", "Transfer"],
            "merchant_category": ["Online", "Grocery", "Fuel"],
            "anomaly_score": ["0.1", "0.9", "0.2"],
            "is_anomaly": ["0", "1", "0"],
        })

    def test_feature_exclusion(self):
        X, cols = build_features(self.test_df)
        # Should not contain is_anomaly or anomaly_score
        self.assertNotIn("is_anomaly", X.columns)
        self.assertNotIn("anomaly_score", X.columns)
        for c in cols:
            self.assertNotIn(c, ["is_anomaly", "anomaly_score"])

    def test_feature_output_shape(self):
        X, cols = build_features(self.test_df)
        self.assertEqual(X.shape[0], 3)
        self.assertTrue(X.shape[1] > 0)
        # All numeric
        for c in X.columns:
            self.assertTrue(np.issubdtype(X[c].dtype, np.number))

    def test_reproducibility(self):
        X1, _ = build_features(self.test_df)
        X2, _ = build_features(self.test_df)
        pd.testing.assert_frame_equal(X1, X2)

    def test_iforest_predictions(self):
        X, _ = build_features(self.test_df)
        model = IsolationForestBaseline(contamination=0.33, random_state=42)
        res = model.fit_predict(X)
        self.assertIn("anomaly_scores", res)
        self.assertIn("flags", res)
        self.assertIn("predictions", res)
        self.assertEqual(len(res["flags"]), 3)
        self.assertEqual(res["contamination"], 0.33)
        # Flags should be 0 or 1
        for f in res["flags"]:
            self.assertIn(f, [0, 1])

    def test_exploratory_compare(self):
        pred = np.array([0, 1, 0])
        true = np.array([0, 1, 0])
        res = exploratory_compare(pred, true)
        self.assertIn("note", res)
        self.assertIn("EXPLORATORY", res["note"])


if __name__ == "__main__":
    unittest.main()
