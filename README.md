# Time-Series Anomaly Detection in Financial Transactions (Academic Prototype)

## Overview
Academic prototype for detecting anomalous financial transactions using time-series data (HCLTech Career Shaper Project 58).

**Important:** 500 rows, only 3 anomalies (0.6%). This is a working academic prototype, not a validated production-grade system. No claim of FPR < 0.1%.

## Dataset
- `dataset.csv`, `data_dictionary.csv` (unchanged)
- Columns: `timestamp`, `account_id`, `trans_amount`, `transaction_type`, `merchant_category`, `anomaly_score`, `is_anomaly`
- Validated: no missing values, no duplicates, timestamps sorted, all values valid

## Installation (already done)
Flask installed for dashboard. Core deps: pandas, numpy, scikit-learn, matplotlib, plotly.

## Run the Dashboard (Flask)
From project root `C:\Users\Dell\Desktop\Financial-Anomaly-Detection`:

```powershell
python -m flask --app dashboard.app run --host 127.0.0.1 --port 5000
```

Then open: **http://127.0.0.1:5000**

Features:
- Dataset overview, transaction types/categories
- Run Isolation Forest with configurable contamination (default 0.01)
- Results table with original transaction fields, model anomaly scores, predicted flags
- Download results CSV (doesn't overwrite original data)
- Warnings about unverified labels and small dataset

## Run EDA
```powershell
python scripts/eda_phase2.py
```

## Run Tests
```powershell
python -m unittest tests.test_data_validation tests.test_phase2 tests.test_phase2_review
```

## Notes
- `is_anomaly` and `anomaly_score` are NOT used as model inputs
- `account_id` and raw timestamps excluded from model features
- Results aligned to original rows
- Autoencoder/LSTM-AE not implemented
- No synthetic data generated

## Status
Dashboard implemented with Flask. All 24 tests pass. EDA runs successfully.
