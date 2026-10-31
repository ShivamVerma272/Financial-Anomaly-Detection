# Create updated compliance matrix
import os
from pathlib import Path

reqs = []
reqs.append(("BRIEF-01","Project Title: Time-Series Anomaly Detection in Financial Transactions"))
reqs.append(("BRIEF-02","Project No. 58"))
reqs.append(("BRIEF-03","Domain: Data Science / Python"))
reqs.append(("BRIEF-04","Skill/Tech Stack: Python, Scikit-learn, TensorFlow, PyTorch, Pandas, Feature Engineering, MLflow"))
reqs.append(("BRIEF-05","Difficulty Level: Advanced"))
reqs.append(("BRIEF-06","Duration: 4 Weeks"))
reqs.append(("BRIEF-07","Format: Individual Project (1 Learner)"))
reqs.append(("BRIEF-08","Academic Year: 2025-26"))
reqs.append(("BRIEF-09","Project Description: Unsupervised anomaly detection (IF, Autoencoder, LSTM-AE)"))
reqs.append(("BRIEF-10","Business Objective with measurable criteria and structured report"))
reqs.append(("BRIEF-11","Deliverable: Completed project (working prototype/application)"))
reqs.append(("BRIEF-12","Deliverable: Project Report - minimum 8 pages (individual)"))
reqs.append(("BRIEF-13","Deliverable: EDA notebook or analysis script with 3+ visualisations"))
reqs.append(("BRIEF-14","Deliverable: dataset.csv cleaned and pre-processed"))
reqs.append(("BRIEF-15","Deliverable: data_dictionary.csv all columns described"))
reqs.append(("BRIEF-16","Deliverable: Demo video (1-2 min) or live demo at expo"))
reqs.append(("BRIEF-17","Deliverable: Signed Ethical Compliance Declaration"))
reqs.append(("BRIEF-18","Week 1: EDA on dataset.csv, mentor approval"))
reqs.append(("BRIEF-19","Week 2: Architecture+core impl, working module demo"))
reqs.append(("BRIEF-20","Week 3: Full integration/testing/validation, metrics recorded"))
reqs.append(("BRIEF-21","Week 4: Report/poster/demo prep, all deliverables submitted"))
reqs.append(("BRIEF-22","Tools/Libraries: Python, TensorFlow/Keras, Scikit-learn, Pandas, Plotly, PyOD"))
reqs.append(("BRIEF-23","Dataset columns specified"))
reqs.append(("BRIEF-24","Dataset_Generation_Prompt.txt reference"))
reqs.append(("BRIEF-25","References section"))
reqs.append(("BRIEF-26","Ethics: FPR < 0.1%, appeal mechanism"))
reqs.append(("BRIEF-27","HCLTech Career Shaper Programme Guidelines"))
reqs.append(("SYN-01","Synopsis: Learner details"))
reqs.append(("SYN-02","Synopsis 1. Problem Statement (5W1H)"))
reqs.append(("SYN-03","Synopsis 2. Proposed Solution & Approach"))
reqs.append(("SYN-04","Synopsis 3. Architecture - DFD Level 0 + system block diagram"))
reqs.append(("SYN-05","Synopsis 4. Technology Stack"))
reqs.append(("SYN-06","Synopsis 5. Dataset Used"))
reqs.append(("SYN-07","Synopsis 6. Key Results & Metrics"))
reqs.append(("SYN-08","Synopsis 7. Challenges & Resolutions"))
reqs.append(("SYN-09","Synopsis 8. References (min 3 credible sources)"))
reqs.append(("SYN-10","Synopsis 9. Ethical Compliance Declaration"))
reqs.append(("SYN-11","Synopsis naming convention"))
reqs.append(("SYN-12","Appendix: AI tools disclosure"))

def st(r):
    if r in ["BRIEF-01","BRIEF-02","BRIEF-03","BRIEF-04","BRIEF-05","BRIEF-06","BRIEF-07","BRIEF-08","BRIEF-09","BRIEF-10","BRIEF-22","BRIEF-23","BRIEF-25","BRIEF-27"]:
        return ("Complete", "From brief")
    if r == "BRIEF-11":
        return ("Missing", "No Project_Report >=8 pages found")
    if r == "BRIEF-12":
        return ("Complete", "scripts/eda_phase2.py + 4 figures in reports/figures/ + reports/eda_findings_phase2.md")
    if r == "BRIEF-13":
        return ("Complete", "dataset.csv exists")
    if r == "BRIEF-14":
        return ("Complete", "data_dictionary.csv complete")
    if r == "BRIEF-15":
        return ("Missing", "No demo video found")
    if r == "BRIEF-16":
        return ("Missing", "No signed Ethics Declaration found")
    if r == "BRIEF-17":
        return ("Complete", "EDA completed")
    if r == "BRIEF-18":
        return ("Partial", "Baseline implemented/tested")
    if r in ["BRIEF-19","BRIEF-20","BRIEF-21","BRIEF-24"]:
        return ("Partial", "In progress/limitations documented")
    if r == "BRIEF-26":
        return ("Partial", "Ethics noted; appeal mechanism/declaration missing; FPR not guaranteed")
    if r.startswith("SYN-"):
        return ("Missing", "Synopsis not filled")
    return ("Partial", "-")

mp = Path('reports/requirements_compliance_matrix_v2.md')
with open(mp,'w',encoding='utf-8') as f:
    f.write("# Requirements Compliance Matrix (Updated)\n\n")
    f.write("Sources: Project_Brief.docx and Project_Synopsis_Template.docx (extracted)\n\n")
    f.write("| Req ID | Requirement | Status | Evidence / Notes |\n")
    f.write("|--------|-------------|--------|------------------|\n")
    for rid,desc in reqs:
        s,n = st(rid)
        f.write(f"| {rid} | {desc} | {s} | {n} |\n")
    c=sum(1 for r in reqs if st(r[0])[0]=='Complete')
    p=sum(1 for r in reqs if st(r[0])[0]=='Partial')
    m=sum(1 for r in reqs if st(r[0])[0]=='Missing')
    nt=sum(1 for r in reqs if st(r[0])[0]=='Noted')
    f.write(f"\n## Summary\n- Complete: {c}\n- Partial: {p}\n- Missing: {m}\n- Noted: {nt}\n- Total: {len(reqs)}\n\n")
    f.write("## Critical Missing Deliverables\n- BRIEF-11: Project Report (minimum 8 pages, individual)\n- BRIEF-15: Demo video (1-2 min) or live demo\n- BRIEF-16: Signed Ethical Compliance Declaration\n- SYN-01 to SYN-12: Filled synopsis with all sections, references >=3, Appendix for AI tools\n- SYN-04: Architecture diagram (DFD Level 0 + system block diagram)\n- Interactive web dashboard (not implemented)\n")

print(mp.resolve())
print(c,p,m,nt)
