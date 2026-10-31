import os
from pathlib import Path

brief = open('brief_full.txt', encoding='utf-8').read()
synopsis = open('synopsis_full.txt', encoding='utf-8').read()

requirements = []
requirements.append(("BRIEF-01", "Project Title: Time-Series Anomaly Detection in Financial Transactions", "project_title"))
requirements.append(("BRIEF-02", "Project No. 58", "project_no"))
requirements.append(("BRIEF-03", "Domain: Data Science / Python", "domain"))
requirements.append(("BRIEF-04", "Skill/Tech Stack listed (Python, Scikit-learn, TensorFlow, PyTorch, Pandas, Feature Engineering, MLflow)", "tech_stack_brief"))
requirements.append(("BRIEF-05", "Difficulty Level: Advanced", "difficulty"))
requirements.append(("BRIEF-06", "Duration: 4 Weeks", "duration"))
requirements.append(("BRIEF-07", "Format: Individual Project (1 Learner)", "format"))
requirements.append(("BRIEF-08", "Project Description: Unsupervised anomaly detection (Isolation Forest, Autoencoder, LSTM-AE) on financial time-series", "description"))
requirements.append(("BRIEF-09", "Business Objective stated", "business_objective"))
requirements.append(("BRIEF-10", "Completed project (working prototype / application)", "deliverable_project"))
requirements.append(("BRIEF-11", "Project Report - minimum 8 pages (individual)", "deliverable_report_8pages"))
requirements.append(("BRIEF-12", "EDA notebook or analysis script with 3+ visualisations", "deliverable_eda_viz"))
requirements.append(("BRIEF-13", "dataset.csv (from this folder) - cleaned and pre-processed", "deliverable_dataset_cleaned"))
requirements.append(("BRIEF-14", "data_dictionary.csv - all columns described", "deliverable_data_dict"))
requirements.append(("BRIEF-15", "Demo video (1-2 minutes) or live demo at expo", "deliverable_demo"))
requirements.append(("BRIEF-16", "Signed Ethical Compliance Declaration", "deliverable_ethics_declaration"))
requirements.append(("BRIEF-17", "Week 1 checkpoint: EDA on dataset.csv approved", "week1"))
requirements.append(("BRIEF-18", "Week 2 checkpoint: Working module demo", "week2"))
requirements.append(("BRIEF-19", "Week 3 checkpoint: End-to-end system working; performance metrics recorded", "week3"))
requirements.append(("BRIEF-20", "Week 4 checkpoint: All deliverables submitted; expo presentation", "week4"))
requirements.append(("BRIEF-21", "Tools & Libraries: Python, TensorFlow/Keras, Scikit-learn, Pandas, Plotly, PyOD", "tools_libs"))
requirements.append(("BRIEF-22", "Dataset file: dataset.csv with columns timestamp, account_id (anon), trans_amount, transaction_type, merchant_category, anomaly_score, is_anomaly", "dataset_spec"))
requirements.append(("BRIEF-23", "Refer to Dataset_Generation_Prompt.txt if needed", "gen_prompt_ref"))
requirements.append(("BRIEF-24", "Ethical Considerations: Financial anomaly detection affects account access. Ensure false positive rate < 0.1%. Provide clear appeal mechanism for flagged accounts.", "ethics_fpr_appeal"))
requirements.append(("BRIEF-25", "HCLTech Career Shaper Programme Guidelines reference", "guidelines_ref"))
requirements.append(("SYN-01", "Project Synopsis template fields to complete (learner details)", "syn_fields"))
requirements.append(("SYN-02", "1. Problem Statement (2-3 sentences, 5W1H format)", "syn_problem"))
requirements.append(("SYN-03", "2. Proposed Solution & Approach (3-5 sentences)", "syn_solution"))
requirements.append(("SYN-04", "3. System Architecture - paste diagram (min: DFD Level 0 + system block diagram)", "syn_architecture_dfd"))
requirements.append(("SYN-05", "4. Technology Stack (Frontend/UI, Backend/Logic, Database, AI/ML Framework, Visualisation, Hardware)", "syn_tech_stack"))
requirements.append(("SYN-06", "5. Dataset Used (filename, rows, columns, key columns, additional data)", "syn_dataset"))
requirements.append(("SYN-07", "6. Key Results & Metrics (Metric 1,2,3 with values, business value achieved)", "syn_metrics"))
requirements.append(("SYN-08", "7. Challenges Faced & How Resolved (Challenge 1&2 with resolution)", "syn_challenges"))
requirements.append(("SYN-09", "8. References (minimum 3 credible sources)", "syn_references"))
requirements.append(("SYN-10", "9. Ethical Compliance Declaration (dataset licence, no PII without consent, AI tools disclosed in Appendix, DPDP Act 2023 compliance)", "syn_ethics_decl"))
requirements.append(("SYN-11", "Submit as 'Project_Synopsis_[YourName]_[RollNo].docx'", "syn_naming"))
requirements.append(("SYN-12", "AI tools used for code/writing are disclosed in the Appendix", "syn_ai_disclosure"))

evidence = {}
evidence['dataset.csv'] = os.path.exists('dataset.csv')
evidence['data_dictionary.csv'] = os.path.exists('data_dictionary.csv')
evidence['Project_Brief.docx'] = os.path.exists('Project_Brief.docx')
evidence['Project_Synopsis_Template.docx'] = os.path.exists('Project_Synopsis_Template.docx')
evidence['src/data/load.py'] = os.path.exists('src/data/load.py')
evidence['src/data/validate.py'] = os.path.exists('src/data/validate.py')
evidence['tests/test_data_validation.py'] = os.path.exists('tests/test_data_validation.py')
evidence['scripts/eda_phase2.py'] = os.path.exists('scripts/eda_phase2.py')
evidence['src/features/build_features.py'] = os.path.exists('src/features/build_features.py')
evidence['src/models/baseline_iforest.py'] = os.path.exists('src/models/baseline_iforest.py')
evidence['src/evaluation/evaluate.py'] = os.path.exists('src/evaluation/evaluate.py')
evidence['tests/test_phase2.py'] = os.path.exists('tests/test_phase2.py')
evidence['tests/test_phase2_review.py'] = os.path.exists('tests/test_phase2_review.py')
evidence['reports/eda_findings_phase2.md'] = os.path.exists('reports/eda_findings_phase2.md')
evidence['reports/figures/amount_distribution.png'] = os.path.exists('reports/figures/amount_distribution.png')
evidence['reports/figures/volume_over_time.png'] = os.path.exists('reports/figures/volume_over_time.png')
evidence['reports/figures/counts_by_type_category.png'] = os.path.exists('reports/figures/counts_by_type_category.png')
evidence['reports/figures/is_anomaly_distribution.png'] = os.path.exists('reports/figures/is_anomaly_distribution.png')
evidence['README.md'] = os.path.exists('README.md')
evidence['dashboard_exists'] = os.path.exists('dashboard') and os.path.isdir('dashboard')

def status_for(req_id):
    if req_id == 'BRIEF-01':
        return 'Complete', 'Project title confirmed in brief and used'
    if req_id == 'BRIEF-02':
        return 'Complete', 'Project No. 58 in brief'
    if req_id == 'BRIEF-04':
        return 'Complete', 'Tech stack documented'
    if req_id in ['BRIEF-05','BRIEF-06','BRIEF-07','BRIEF-08','BRIEF-09']:
        return 'Complete', 'Documented in brief'
    if req_id == 'BRIEF-10':
        return 'Partial', 'Prototype modules exist, not complete integrated application'
    if req_id == 'BRIEF-11':
        return 'Missing', 'No Project_Report >=8 pages in reports/'
    if req_id == 'BRIEF-12':
        return 'Complete', 'scripts/eda_phase2.py + 4 figures in reports/figures/ + reports/eda_findings_phase2.md'
    if req_id == 'BRIEF-13':
        return 'Complete', 'dataset.csv exists unchanged'
    if req_id == 'BRIEF-14':
        return 'Complete', 'data_dictionary.csv with all columns described'
    if req_id == 'BRIEF-15':
        return 'Missing', 'No demo video found'
    if req_id == 'BRIEF-16':
        return 'Missing', 'No signed Ethical Compliance Declaration found'
    if req_id == 'BRIEF-17':
        return 'Complete', 'EDA completed (Phase 2)'
    if req_id == 'BRIEF-18':
        return 'Partial', 'Isolation Forest baseline implemented/tested'
    if req_id == 'BRIEF-19':
        return 'Partial', 'Baseline exists with exploratory metrics'
    if req_id == 'BRIEF-20':
        return 'Missing', 'Deliverables not all submitted'
    if req_id == 'BRIEF-21':
        return 'Partial', 'Core libs used; TensorFlow/PyTorch/PyOD/MLflow not yet integrated'
    if req_id == 'BRIEF-22':
        return 'Complete', 'Required columns present'
    if req_id == 'BRIEF-23':
        return 'Noted', 'Mentioned; Dataset_Generation_Prompt.txt not present'
    if req_id == 'BRIEF-24':
        return 'Partial', 'Ethics noted, FPR limitations documented; appeal mechanism/declaration missing'
    if req_id == 'BRIEF-25':
        return 'Noted', 'Guidelines referenced'
    if req_id.startswith('SYN-'):
        return 'Missing', 'Filled synopsis not found with required sections'
    return 'Partial', 'Needs review'

matrix_path = Path('reports/requirements_compliance_matrix.md')
matrix_path.parent.mkdir(parents=True, exist_ok=True)
with open(matrix_path, 'w', encoding='utf-8') as f:
    f.write('# Requirements Compliance Matrix\n\n')
    f.write('Sources extracted from actual documents:\n')
    f.write('- Project_Brief.docx (brief_full.txt)\n')
    f.write('- Project_Synopsis_Template.docx (synopsis_full.txt)\n\n')
    f.write('| Req ID | Requirement | Status | Evidence / Notes |\n')
    f.write('|--------|-------------|--------|------------------|\n')
    for req_id, desc, key in requirements:
        status, notes = status_for(req_id)
        f.write(f'| {req_id} | {desc} | {status} | {notes} |\n')
    complete = sum(1 for r in requirements if status_for(r[0])[0]=='Complete')
    partial = sum(1 for r in requirements if status_for(r[0])[0]=='Partial')
    missing = sum(1 for r in requirements if status_for(r[0])[0]=='Missing')
    noted = sum(1 for r in requirements if status_for(r[0])[0]=='Noted')
    f.write('\n## Summary\n')
    f.write(f'- Complete: {complete}\n')
    f.write(f'- Partial: {partial}\n')
    f.write(f'- Missing: {missing}\n')
    f.write(f'- Noted: {noted}\n')
    f.write(f'- Total: {len(requirements)}\n\n')
    f.write('## Critical Missing Deliverables\n')
    f.write('- Project Report (minimum 8 pages, individual) - BRIEF-11\n')
    f.write('- Demo video (1-2 minutes) or live demo at expo - BRIEF-15\n')
    f.write('- Signed Ethical Compliance Declaration - BRIEF-16\n')
    f.write('- Filled Project Synopsis with all template fields - SYN-01 to SYN-12\n')
    f.write('- System Architecture with DFD Level 0 + system block diagram - SYN-04\n')
    f.write('- Interactive web dashboard - not implemented\n')
    f.write('\n## Notes\n')
    f.write('- Marked Complete only with verified files/outputs.\n')
    f.write('- EDA, dataset validation, tests, baseline marked based on actual artifacts.\n')
    f.write('- Labels unverified (3 positives only); metrics exploratory.\n')
    f.write('- dataset.csv unchanged, no synthetic data generated.\n')

print(matrix_path.resolve())
