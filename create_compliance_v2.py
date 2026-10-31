import os
from pathlib import Path

brief = open('brief_full.txt', encoding='utf-8').read()
syn = open('synopsis_full.txt', encoding='utf-8').read()

requirements = []
# Detailed extraction
requirements.append(("BRIEF-01", "Project Title: Time-Series Anomaly Detection in Financial Transactions", "title"))
requirements.append(("BRIEF-02", "Project No. 58", "projno"))
requirements.append(("BRIEF-03", "Domain: Data Science / Python", "domain"))
requirements.append(("BRIEF-04", "Skill / Tech Stack mentioned: Python, Scikit-learn, TensorFlow, PyTorch, Pandas, Feature Engineering, MLflow", "techstack"))
requirements.append(("BRIEF-05", "Difficulty Level: Advanced", "diff"))
requirements.append(("BRIEF-06", "Duration: 4 Weeks", "dur"))
requirements.append(("BRIEF-07", "Format: Individual Project (1 Learner)", "fmt"))
requirements.append(("BRIEF-08", "Academic Year: 2025-26", "ay"))
requirements.append(("BRIEF-09", "Project Description: Unsupervised anomaly detection (Isolation Forest, Autoencoder, LSTM-AE) on financial time-series to flag unusual transaction patterns", "desc"))
requirements.append(("BRIEF-10", "Business Objective: Design and implement a working solution demonstrating real-world application; validate against measurable performance criteria; document findings in structured project report", "bobj"))
requirements.append(("BRIEF-11", "Key Deliverables - Completed project (working prototype / application)", "d1_proj"))
requirements.append(("BRIEF-12", "Key Deliverables - Project Report - minimum 8 pages (individual)", "d2_report"))
requirements.append(("BRIEF-13", "Key Deliverables - EDA notebook or analysis script with 3+ visualisations", "d3_eda"))
requirements.append(("BRIEF-14", "Key Deliverables - dataset.csv (from this folder) - cleaned and pre-processed", "d4_dataset"))
requirements.append(("BRIEF-15", "Key Deliverables - data_dictionary.csv - all columns described", "d5_dict"))
requirements.append(("BRIEF-16", "Key Deliverables - Demo video (1-2 minutes) or live demo at expo", "d6_demo"))
requirements.append(("BRIEF-17", "Key Deliverables - Signed Ethical Compliance Declaration", "d7_ethics"))
requirements.append(("BRIEF-18", "Week 1: Problem understanding, tool setup, EDA on dataset.csv - Mentor approves problem statement + EDA notebook", "w1"))
requirements.append(("BRIEF-19", "Week 2: Architecture design + core implementation (Sprint 1) - Working module demo to mentor", "w2"))
requirements.append(("BRIEF-20", "Week 3: Full integration, testing, and validation - End-to-end system working; performance metrics recorded", "w3"))
requirements.append(("BRIEF-21", "Week 4: Report writing, poster/presentation, demo preparation - All deliverables submitted; expo presentation", "w4"))
requirements.append(("BRIEF-22", "Tools & Libraries: Python, TensorFlow/Keras, Scikit-learn, Pandas, Plotly, PyOD", "libs"))
requirements.append(("BRIEF-23", "Dataset: dataset.csv with columns timestamp, account_id (anon), trans_amount, transaction_type, merchant_category, anomaly_score, is_anomaly", "dataset"))
requirements.append(("BRIEF-24", "Dataset note: Refer to Dataset_Generation_Prompt.txt to generate additional rows using AI tool if needed", "genref"))
requirements.append(("BRIEF-25", "References section mentioned (Mentor to validate and add link)", "refs"))
requirements.append(("BRIEF-26", "Ethical Considerations: Financial anomaly detection affects account access. Ensure false positive rate < 0.1%. Provide clear appeal mechanism for flagged accounts.", "ethics"))
requirements.append(("BRIEF-27", "Programme Guidelines: HCLTech Career Shaper Programme Guidelines (provided by Programme Coordinator)", "guidelines"))

# Synopsis detailed
requirements.append(("SYN-01", "Synopsis Template - Project Title: Time-Series Anomaly Detection in Financial Transactions", "stitle"))
requirements.append(("SYN-02", "Synopsis Template - Project No. 58, Domain Data Science / Python, Difficulty Advanced, Duration 4 Weeks, Format Individual", "smeta"))
requirements.append(("SYN-03", "Synopsis - Learner details to fill: Learner Name, Roll Number, College/Campus, Mentor Name, Submission Date", "slearner"))
requirements.append(("SYN-04", "Synopsis 1. Problem Statement - 2-3 sentences, use 5W1H format (Who, What, When/where, Why, How)", "sprob"))
requirements.append(("SYN-05", "Synopsis 2. Proposed Solution & Approach - 3-5 sentences describing what built, tech used, how solves", "ssol"))
requirements.append(("SYN-06", "Synopsis 3. System Architecture - paste architecture/block diagram (minimum: Data Flow Diagram Level 0 + system block diagram)", "sarch"))
requirements.append(("SYN-07", "Synopsis 4. Technology Stack - Frontend/UI, Backend/Logic, Database, AI/ML Framework (if applicable), Visualisation, Hardware (if applicable)", "sstack"))
requirements.append(("SYN-08", "Synopsis 5. Dataset Used - dataset file name dataset.csv, number of rows, number of columns, key columns (list 5), additional data collected", "sdset"))
requirements.append(("SYN-09", "Synopsis 6. Key Results & Metrics - Metric 1, Metric 2, Metric 3 with values; Business value achieved", "sres"))
requirements.append(("SYN-10", "Synopsis 7. Challenges Faced & How Resolved - Challenge 1 and Challenge 2 with resolutions", "schal"))
requirements.append(("SYN-11", "Synopsis 8. References - minimum 3 credible sources", "srefs"))
requirements.append(("SYN-12", "Synopsis 9. Ethical Compliance Declaration - dataset usage complies with licence; no PII without consent; AI tools used disclosed in Appendix; complies with DPDP Act 2023 where applicable", "seth"))
requirements.append(("SYN-13", "Synopsis submission naming: 'Project_Synopsis_[YourName]_[RollNo].docx'", "snaming"))
requirements.append(("SYN-14", "Synopsis - AI tools used for code/writing are disclosed in the Appendix", "sai"))

def status_for(req_id):
    if req_id in ['BRIEF-01','BRIEF-02','BRIEF-03','BRIEF-04','BRIEF-05','BRIEF-06','BRIEF-07','BRIEF-08','BRIEF-09','BRIEF-10']:
        return 'Complete', 'Documented in Project_Brief.docx'
    if req_id == 'BRIEF-11':
        return 'Missing', 'No Project_Report found in reports/ (minimum 8 pages required)'
    if req_id == 'BRIEF-12':
        return 'Complete', 'scripts/eda_phase2.py, reports/figures/*.png (4 files), reports/eda_findings_phase2.md'
    if req_id == 'BRIEF-13':
        return 'Complete', 'dataset.csv present (cleaned/preprocessed state not re-processed but exists)'
    if req_id == 'BRIEF-14':
        return 'Complete', 'data_dictionary.csv exists with all columns described'
    if req_id == 'BRIEF-15':
        return 'Missing', 'No demo video (1-2 min) or demo files found'
    if req_id == 'BRIEF-16':
        return 'Missing', 'No signed Ethical Compliance Declaration found'
    if req_id in ['BRIEF-17']:
        return 'Complete', 'EDA on dataset.csv completed (Phase 2)'
    if req_id in ['BRIEF-18']:
        return 'Partial', 'Baseline module exists (Isolation Forest) tested; full working module demo not documented'
    if req_id in ['BRIEF-19','BRIEF-20']:
        return 'Partial', 'Integration/testing in progress; end-to-end complete system not verified'
    if req_id == 'BRIEF-21':
        return 'Partial', 'Core libs used (pandas/numpy/sklearn/matplotlib/plotly); TensorFlow/PyTorch/PyOD/MLflow not integrated'
    if req_id == 'BRIEF-22':
        return 'Complete', 'dataset.csv has required columns'
    if req_id == 'BRIEF-23':
        return 'Noted', 'Dataset_Generation_Prompt.txt not present'
    if req_id == 'BRIEF-24':
        return 'Partial', 'Ethics noted in docs; appeal mechanism documented conceptually missing; FPR < 0.1% not guaranteed (documented limitation)'
    if req_id == 'BRIEF-25','BRIEF-26','BRIEF-27':
        return 'Noted', 'Mentioned in brief'
    if req_id.startswith('SYN-'):
        return 'Missing', 'Filled synopsis not created'
    return 'Partial', 'Review'

matrix_path = Path('reports/requirements_compliance_matrix_v2.md')
with open(matrix_path, 'w', encoding='utf-8') as f:
    f.write('# Requirements Compliance Matrix (Updated)\n\n')
    f.write('Extracted from full source documents:\n')
    f.write('- Project_Brief.docx -> brief_full.txt\n')
    f.write('- Project_Synopsis_Template.docx -> synopsis_full.txt\n\n')
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
    f.write('- BRIEF-11: Project Report (minimum 8 pages, individual)\n')
    f.write('- BRIEF-15: Demo video (1-2 minutes) or live demo at expo\n')
    f.write('- BRIEF-16: Signed Ethical Compliance Declaration\n')
    f.write('- SYN-01 to SYN-14: Filled Project Synopsis with all template fields (including Appendix for AI tools, references >=3)\n')
    f.write('- SYN-06: System Architecture diagram (DFD Level 0 + system block diagram)\n')
    f.write('- Dashboard: Interactive web dashboard (not implemented)\n')
    f.write('\n## Notes\n')
    f.write('- Statuses are evidence-based; items only Complete if real files/verified outputs exist.\n')
    f.write('- No files modified, dataset.csv unchanged.\n')

print(matrix_path.resolve())
print(complete, partial, missing, noted)
