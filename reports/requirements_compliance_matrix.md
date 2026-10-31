# Requirements Compliance Matrix

Sources extracted from actual documents:
- Project_Brief.docx (brief_full.txt)
- Project_Synopsis_Template.docx (synopsis_full.txt)

| Req ID | Requirement | Status | Evidence / Notes |
|--------|-------------|--------|------------------|
| BRIEF-01 | Project Title: Time-Series Anomaly Detection in Financial Transactions | Complete | Project title confirmed in brief and used |
| BRIEF-02 | Project No. 58 | Complete | Project No. 58 in brief |
| BRIEF-03 | Domain: Data Science / Python | Partial | Needs review |
| BRIEF-04 | Skill/Tech Stack listed (Python, Scikit-learn, TensorFlow, PyTorch, Pandas, Feature Engineering, MLflow) | Complete | Tech stack documented |
| BRIEF-05 | Difficulty Level: Advanced | Complete | Documented in brief |
| BRIEF-06 | Duration: 4 Weeks | Complete | Documented in brief |
| BRIEF-07 | Format: Individual Project (1 Learner) | Complete | Documented in brief |
| BRIEF-08 | Project Description: Unsupervised anomaly detection (Isolation Forest, Autoencoder, LSTM-AE) on financial time-series | Complete | Documented in brief |
| BRIEF-09 | Business Objective stated | Complete | Documented in brief |
| BRIEF-10 | Completed project (working prototype / application) | Partial | Prototype modules exist, not complete integrated application |
| BRIEF-11 | Project Report - minimum 8 pages (individual) | Missing | No Project_Report >=8 pages in reports/ |
| BRIEF-12 | EDA notebook or analysis script with 3+ visualisations | Complete | scripts/eda_phase2.py + 4 figures in reports/figures/ + reports/eda_findings_phase2.md |
| BRIEF-13 | dataset.csv (from this folder) - cleaned and pre-processed | Complete | dataset.csv exists unchanged |
| BRIEF-14 | data_dictionary.csv - all columns described | Complete | data_dictionary.csv with all columns described |
| BRIEF-15 | Demo video (1-2 minutes) or live demo at expo | Missing | No demo video found |
| BRIEF-16 | Signed Ethical Compliance Declaration | Missing | No signed Ethical Compliance Declaration found |
| BRIEF-17 | Week 1 checkpoint: EDA on dataset.csv approved | Complete | EDA completed (Phase 2) |
| BRIEF-18 | Week 2 checkpoint: Working module demo | Partial | Isolation Forest baseline implemented/tested |
| BRIEF-19 | Week 3 checkpoint: End-to-end system working; performance metrics recorded | Partial | Baseline exists with exploratory metrics |
| BRIEF-20 | Week 4 checkpoint: All deliverables submitted; expo presentation | Missing | Deliverables not all submitted |
| BRIEF-21 | Tools & Libraries: Python, TensorFlow/Keras, Scikit-learn, Pandas, Plotly, PyOD | Partial | Core libs used; TensorFlow/PyTorch/PyOD/MLflow not yet integrated |
| BRIEF-22 | Dataset file: dataset.csv with columns timestamp, account_id (anon), trans_amount, transaction_type, merchant_category, anomaly_score, is_anomaly | Complete | Required columns present |
| BRIEF-23 | Refer to Dataset_Generation_Prompt.txt if needed | Noted | Mentioned; Dataset_Generation_Prompt.txt not present |
| BRIEF-24 | Ethical Considerations: Financial anomaly detection affects account access. Ensure false positive rate < 0.1%. Provide clear appeal mechanism for flagged accounts. | Partial | Ethics noted, FPR limitations documented; appeal mechanism/declaration missing |
| BRIEF-25 | HCLTech Career Shaper Programme Guidelines reference | Noted | Guidelines referenced |
| SYN-01 | Project Synopsis template fields to complete (learner details) | Missing | Filled synopsis not found with required sections |
| SYN-02 | 1. Problem Statement (2-3 sentences, 5W1H format) | Missing | Filled synopsis not found with required sections |
| SYN-03 | 2. Proposed Solution & Approach (3-5 sentences) | Missing | Filled synopsis not found with required sections |
| SYN-04 | 3. System Architecture - paste diagram (min: DFD Level 0 + system block diagram) | Missing | Filled synopsis not found with required sections |
| SYN-05 | 4. Technology Stack (Frontend/UI, Backend/Logic, Database, AI/ML Framework, Visualisation, Hardware) | Missing | Filled synopsis not found with required sections |
| SYN-06 | 5. Dataset Used (filename, rows, columns, key columns, additional data) | Missing | Filled synopsis not found with required sections |
| SYN-07 | 6. Key Results & Metrics (Metric 1,2,3 with values, business value achieved) | Missing | Filled synopsis not found with required sections |
| SYN-08 | 7. Challenges Faced & How Resolved (Challenge 1&2 with resolution) | Missing | Filled synopsis not found with required sections |
| SYN-09 | 8. References (minimum 3 credible sources) | Missing | Filled synopsis not found with required sections |
| SYN-10 | 9. Ethical Compliance Declaration (dataset licence, no PII without consent, AI tools disclosed in Appendix, DPDP Act 2023 compliance) | Missing | Filled synopsis not found with required sections |
| SYN-11 | Submit as 'Project_Synopsis_[YourName]_[RollNo].docx' | Missing | Filled synopsis not found with required sections |
| SYN-12 | AI tools used for code/writing are disclosed in the Appendix | Missing | Filled synopsis not found with required sections |

## Summary
- Complete: 13
- Partial: 6
- Missing: 16
- Noted: 2
- Total: 37

## Critical Missing Deliverables
- Project Report (minimum 8 pages, individual) - BRIEF-11
- Demo video (1-2 minutes) or live demo at expo - BRIEF-15
- Signed Ethical Compliance Declaration - BRIEF-16
- Filled Project Synopsis with all template fields - SYN-01 to SYN-12
- System Architecture with DFD Level 0 + system block diagram - SYN-04
- Interactive web dashboard - not implemented

## Notes
- Marked Complete only with verified files/outputs.
- EDA, dataset validation, tests, baseline marked based on actual artifacts.
- Labels unverified (3 positives only); metrics exploratory.
- dataset.csv unchanged, no synthetic data generated.
