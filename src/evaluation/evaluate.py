"""
Evaluation helpers for unsupervised anomaly detection.
"""
from __future__ import annotations

import numpy as np
from typing import Dict, Any


def exploratory_compare(pred_flags: np.ndarray, true_labels: np.ndarray) -> Dict[str, Any]:
    """
    Exploratory comparison only. 
    true_labels may be is_anomaly (0/1). Provenance unknown, n_pos small.
    """
    pred_flags = np.array(pred_flags).astype(int)
    true_labels = np.array(true_labels).astype(int)
    n = len(pred_flags)
    n_pos_true = int((true_labels == 1).sum())
    n_flagged = int((pred_flags == 1).sum())
    # confusion matrix
    tp = int(((pred_flags == 1) & (true_labels == 1)).sum())
    fp = int(((pred_flags == 1) & (true_labels == 0)).sum())
    tn = int(((pred_flags == 0) & (true_labels == 0)).sum())
    fn = int(((pred_flags == 0) & (true_labels == 1)).sum())
    result = {
        "note": "EXPLORATORY ONLY - label provenance unknown, only 3 positive labels exist; not a reliable estimate of performance",
        "n": n,
        "n_true_positives": n_pos_true,
        "n_flagged": n_flagged,
        "tp": tp,
        "fp": fp,
        "tn": tn,
        "fn": fn,
    }
    # metrics only if meaningful
    if (tp + fp) > 0:
        result["precision"] = tp / (tp + fp)
    if (tp + fn) > 0:
        result["recall"] = tp / (tp + fn)
    if ("precision" in result and "recall" in result and (result["precision"] + result["recall"]) > 0):
        result["f1"] = 2 * result["precision"] * result["recall"] / (result["precision"] + result["recall"])
    if (tn + fp) > 0:
        result["fpr"] = fp / (tn + fp)  # false positive rate
    result["disclaimer"] = "Do not claim FPR < 0.1% or reliable performance from this small/unverified label set."
    return result
