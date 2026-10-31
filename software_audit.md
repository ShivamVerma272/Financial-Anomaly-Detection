# Software Compliance Audit - Project 58

## Tests
- Command: `python -m unittest tests.test_data_validation tests.test_phase2 tests.test_phase2_review`
- Result: **Ran 24 tests in 2.594s - OK**

## Workflow verification
- Dataset loading: `src/data/load.py` - loads CSV, validates file existence/format
- Validation: `src/data/validate.py` - schema, timestamps, numerics, is_anomaly values, duplicates
- Feature engineering: `src/features/build_features.py` - excludes is_anomaly/anomaly_score, excludes account_id/raw timestamp, handles NaN/non-finite
- Model: `src/models/baseline_iforest.py` - Isolation Forest, configurable contamination, returns scores/flags
- Results: Dashboard displays flagged transactions with original fields + model scores
- Download: CSV saved to `reports/dashboard_results.csv`, download endpoint works

## EDA
- `scripts/eda_phase2.py` generates 4 visualizations: amount distribution, volume over time, counts by type/category, is_anomaly distribution
- Saved to `reports/figures/`

## Autoencoder/LSTM-AE
- **Not implemented**. Brief mentions them as possible approaches but they are not required to be implemented - brief says "Unsupervised anomaly detection (Isolation Forest, Autoencoder, LSTM-AE)" as description of techniques; current implementation uses Isolation Forest as baseline. Not missing if only baseline required. No AE/LSTM-AE code exists.

## Evaluation/Claims
- No claims of FPR < 0.1% made
- Labels marked as unverified provenance, only 3 positives noted
- Exploratory comparison only if used

## Appeal mechanism
- Brief states "Provide clear appeal mechanism for flagged accounts" - this is a process/documentation requirement, not a software feature. Not implemented in code; would need to be in report/documentation.

## Data integrity
- dataset.csv unchanged
- data_dictionary.csv unchanged
- No synthetic data generated

## Dashboard workflow test
- GET /: 200 OK
- POST /run: 200 OK
- GET /download: 200 OK (after running detection)

## Next software tasks
1. Add more robust error handling in dashboard for edge cases
2. Consider adding model performance metrics display (with appropriate warnings)
3. Add option to view all results vs flagged only
4. Improve visualizations in dashboard
