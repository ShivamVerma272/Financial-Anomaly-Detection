"""
Isolation Forest baseline (unsupervised). 
Does not use is_anomaly or anomaly_score as inputs.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from typing import Dict, Any


class IsolationForestBaseline:
    def __init__(self, contamination: float = 0.01, random_state: int = 42, n_estimators: int = 100):
        if not isinstance(contamination, (int, float)) or isinstance(contamination, bool):
            raise ValueError("contamination must be a number")
        if contamination < 0 or contamination > 0.5:
            raise ValueError("contamination must be between 0 and 0.5")
        self.contamination = float(contamination)
        self.random_state = int(random_state)
        self.n_estimators = int(n_estimators)
        from sklearn.ensemble import IsolationForest

        self.model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state,
            n_estimators=self.n_estimators,
        )
        self.is_fitted = False

    def fit_predict(self, X: pd.DataFrame | np.ndarray) -> Dict[str, Any]:
        if isinstance(X, pd.DataFrame):
            X_arr = X.values
        else:
            X_arr = np.array(X)
        if X_arr.size == 0:
            raise ValueError("Empty input")
        if X_arr.shape[0] < 1:
            raise ValueError("Need at least 1 row")
        # Check finite
        if not np.all(np.isfinite(X_arr)):
            raise ValueError("Non-finite values in input")
        self.model.fit(X_arr)
        self.is_fitted = True
        scores = self.model.decision_function(X_arr)
        anomaly_scores = -scores
        preds = self.model.predict(X_arr)
        flags = (preds == -1).astype(int)
        return {
            "anomaly_scores": anomaly_scores,
            "predictions": preds,
            "flags": flags,
            "contamination": self.contamination,
        }
