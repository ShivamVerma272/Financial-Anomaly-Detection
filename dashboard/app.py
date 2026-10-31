import os
from pathlib import Path
from flask import Flask, render_template, request, send_file
import pandas as pd

from src.features.build_features import build_features
from src.models.baseline_iforest import IsolationForestBaseline

app = Flask(__name__)

DATA_PATH = Path(__file__).parent.parent / "dataset.csv"
RESULTS_PATH = Path(__file__).parent.parent / "reports" / "dashboard_results.csv"

@app.route('/')
def index():
    try:
        df = pd.read_csv(DATA_PATH)
        overview = {
            "rows": len(df),
            "cols": len(df.columns),
            "transaction_types": df["transaction_type"].value_counts().to_dict(),
            "merchant_categories": df["merchant_category"].value_counts().to_dict(),
        }
        df2 = df.copy()
        df2["timestamp"] = pd.to_datetime(df2["timestamp"], errors="coerce")
        vol = df2.groupby(df2["timestamp"].dt.date).size().to_dict()
        vol = {str(k): int(v) for k, v in vol.items()}
        amounts = df["trans_amount"].astype(float).tolist()
        return render_template('index.html', overview=overview, amounts=amounts, vol=vol)
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/run', methods=['POST'])
def run_detection():
    try:
        contamination_raw = request.form.get('contamination', '0.01')
        try:
            contamination = float(contamination_raw)
        except Exception:
            return render_template('error.html', error='Invalid contamination value. Must be a number between 0 and 0.5.')
        if contamination < 0 or contamination > 0.5:
            return render_template('error.html', error='Contamination must be between 0 and 0.5.')
        df = pd.read_csv(DATA_PATH)
        X, cols, row_id, report = build_features(df, return_metadata=True)
        model = IsolationForestBaseline(contamination=contamination, random_state=42)
        res = model.fit_predict(X)
        results = df.copy()
        results['anomaly_score_model'] = res['anomaly_scores']
        results['predicted_flag'] = res['flags']
        RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
        results.to_csv(RESULTS_PATH, index=False)
        flagged = int(results['predicted_flag'].sum())
        unflagged = int(len(results) - flagged)
        return render_template('results.html', 
                             results=results.to_dict('records'),
                             flagged=flagged,
                             unflagged=unflagged,
                             contamination=contamination)
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/download')
def download():
    try:
        if RESULTS_PATH.exists():
            return send_file(str(RESULTS_PATH), as_attachment=True, download_name='anomaly_results.csv')
        return render_template('error.html', error='No results available. Run detection first.')
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
