#!/usr/bin/env python3
import argparse, os
from src.engine.ingest import read_input
from src.engine.transform import summarize_data
from src.engine.ai import generate_narrative
from src.engine.report import build_pptx
from src.engine.pdf import convert_pptx_to_pdf
from src.engine.charts import create_line_chart, create_bar_chart

def main():
    parser = argparse.ArgumentParser(description='Run Automated Insight Engine pipeline.')
    parser.add_argument('--input', '-i', required=True, help='Path to CSV file or SQL URL')
    parser.add_argument('--output', '-o', required=True, help='Base name for outputs (no extension)')
    parser.add_argument('--title', '-t', default='Automated Insight Report', help='Report title')
    parser.add_argument('--llm', action='store_true', help='Use LLM if OPENAI_API_KEY is set')
    parser.add_argument('--pdf', action='store_true', help='Generate PDF via LibreOffice if installed')
    args = parser.parse_args()

    # Root and outputs
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    OUTPUT_DIR = os.path.abspath(os.path.join(ROOT, "..", "outputs"))
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    base = os.path.basename(args.output)
    pptx_path = os.path.join(OUTPUT_DIR, base + ".pptx")
    pdf_path = os.path.join(OUTPUT_DIR, base + ".pdf")

    print("[INFO] Ingesting data...")
    df = read_input(args.input)

    print("[INFO] Summarizing data...")
    summary = summarize_data(df)

    print("[INFO] Generating narrative...")
    narrative = generate_narrative(summary, use_llm=args.llm)

    print("[INFO] Generating charts...")
    charts_dir = os.path.join(OUTPUT_DIR, "charts")
    os.makedirs(charts_dir, exist_ok=True)
    charts = {}
    # create example charts if columns exist
    if 'date' in df.columns and 'impressions' in df.columns:
        line_path = os.path.join(charts_dir, base + "_impressions.png")
        create_line_chart(df, 'date', 'impressions', line_path)
        charts['Impressions Over Time'] = line_path
    if 'campaign' in df.columns and 'spend' in df.columns:
        bar_path = os.path.join(charts_dir, base + "_spend.png")
        create_bar_chart(df, 'campaign', 'spend', bar_path)
        charts['Spend by Campaign'] = bar_path

    print("[INFO] Building PPTX...")
    template_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'ppt_template.pptx')
    # if template missing, build_pptx will fallback to blank ppt
    build_pptx(pptx_path, title=args.title, summary=[f"Rows: {summary.get('rows')}",], narrative=narrative, charts=charts, template_path=template_path)

    if args.pdf:
        print("[INFO] Attempting PDF conversion...")
        convert_pptx_to_pdf(pptx_path, pdf_path)

    print(f"[SUCCESS] PPTX: {pptx_path}")
    if args.pdf:
        print(f"[SUCCESS] PDF: {pdf_path}")


if __name__ == '__main__':
    main()
