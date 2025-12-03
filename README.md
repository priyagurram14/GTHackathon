# Automated Insight Engine (Hackathon Prototype)

A fully automated data-to-insight pipeline that ingests raw data, analyzes it, generates AI-powered executive insights, and exports formatted PowerPoint and PDF reports — all without human intervention.

---

## 🚀 Features

- **Multi-source ingestion**
  - CSV files
  - SQL databases (via SQLAlchemy URLs)

- **Automated transformations**
  - Summary statistics
  - KPI extraction
  - Missing-value analysis

- **AI-powered narrative (optional)**
  - Uses OpenAI GPT when `OPENAI_API_KEY` is available
  - Falls back to template-based summaries otherwise

- **Automated reporting**
  - Generates a fully formatted PPTX using `python-pptx`
  - Optional PDF export via LibreOffice headless mode
  - Graceful fallback when LibreOffice is not installed

- **Cross-platform compatibility**
  - Windows, macOS, Linux

- **Simple CLI interface**
  - One command runs the full end-to-end pipeline

---

## 🛠 Installation

### 1. Create a virtual environment and install dependencies

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 🔑 (Optional) Enable AI Narrative Generation

Get an OpenAI API key:
https://platform.openai.com/settings/organization/api-keys

Set the key:

**Windows:**
```powershell
setx OPENAI_API_KEY "sk-your-key-here"
```

**macOS / Linux:**
```bash
export OPENAI_API_KEY="sk-your-key-here"
```

Restart your terminal after setting the key.

---

## ⚡ Running the Engine

### Generate PPTX (LLM optional)
```bash
python cli.py --input examples/adtech_sample.csv --output outputs/report --llm
```

Produces:
```
outputs/report.pptx
```

---

### Generate PDF (LibreOffice required)
```bash
python cli.py --input examples/adtech_sample.csv --output outputs/report --llm --pdf
```

If LibreOffice is installed, this also generates:
```
outputs/report.pdf
```

If LibreOffice is missing:
- A warning is shown  
- PPTX is still generated  
- PDF step is skipped safely  

---

## 📁 Project Structure

```
automated-insight-engine/
│
├── src/
│   └── engine/
│       ├── ingest.py
│       ├── transform.py
│       ├── ai.py
│       ├── report.py
│       └── pdf.py
│
├── examples/
├── outputs/
├── cli.py
├── requirements.txt
└── README.md
```

---

## 🧪 Testing

Run tests:
```bash
pytest -q
```

### GitHub Actions CI

A CI workflow is included.

To enable PDF export in CI, add:
```yaml
- name: Install LibreOffice
  run: sudo apt-get update && sudo apt-get install -y libreoffice
```

---

## 📄 License

MIT License
