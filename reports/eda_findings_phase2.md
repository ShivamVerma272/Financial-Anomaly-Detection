# EDA Findings (Phase 2)
Dataset: dataset.csv (loaded without modification)
Shape: 500 rows, 8 columns

## Basic Statistics
- Rows: 500
- Unique accounts: 468
- Date range: 2024-01-01 00:26:00 to 2024-01-06 09:10:00
- Transaction amount - min: 6.07, max: 1471.92, mean: 152.04, median: 92.62
- Anomaly score - min: 0.0043, max: 0.9978, mean: 0.5187

## Class Distribution (is_anomaly)
- is_anomaly=0: 497 (99.40%)
- is_anomaly=1: 3 (0.60%)

**Note:** Only 3 positive labels (0.6%). Provenance unknown - do not treat as verified ground truth.

## Transaction Types
- Transfer: 172
- Debit: 168
- Credit: 160

## Merchant Categories
- Travel: 101
- Online: 86
- Fuel: 86
- Electronics: 82
- Grocery: 80
- Restaurant: 65

## Figures Generated
- reports/figures/amount_distribution.png
- reports/figures/volume_over_time.png
- reports/figures/counts_by_type_category.png
- reports/figures/is_anomaly_distribution.png
