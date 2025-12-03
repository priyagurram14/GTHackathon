from flask import Flask, request, render_template, send_file, redirect, url_for
import os, pandas as pd
from src.engine.transform import summarize_data
from src.engine.ai import generate_narrative
from src.engine.report import build_pptx

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('file')
    if not f:
        return redirect(url_for('index'))
    df = pd.read_csv(f)
    summary = summarize_data(df)
    narrative = generate_narrative(summary, use_llm=False)
    OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'outputs'))
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_pptx = os.path.join(OUTPUT_DIR, 'web_report.pptx')
    build_pptx(out_pptx, title='Web Upload Report', summary=summary, narrative=narrative, charts=None, template_path=None)
    return send_file(out_pptx, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
