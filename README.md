# Automated Insight Engine (Premium Hackathon Edition)

A complete **end-to-end automated analytics system** that ingests raw data, analyzes it, generates AI-powered insights, builds charts, applies branded slide templates, and exports polished PowerPoint & PDF reports — all automatically and reproducibly.

This premium edition also includes a **web UI for uploading datasets** and a fully modular **engine** designed for hackathon demos and production-ready extensibility.

---

# ✨ Key Features

### 🔹 Multi-source Data Ingestion  
- CSV files  
- SQL databases (via SQLAlchemy URLs)

### 🔹 Automated Data Analysis  
- Summary statistics  
- Column profiling  
- KPI extraction  
- Missing-value analysis  
- Numeric describe() breakdowns  

### 🔹 AI-Generated Executive Narratives (Optional)  
- Uses OpenAI GPT if `OPENAI_API_KEY` is set  
- Local fallback narrative generator if key is missing  

### 🔹 Beautiful Chart Generation  
- Line charts  
- Bar charts  
- Auto-saved into `/outputs/charts/`

### 🔹 Premium PPTX Report Builder  
- Branded template support (`ppt_template.pptx`)  
- Executive Summary slide  
- Data Summary slide  
- Auto-embedded charts  
- Fully customizable layouts  

### 🔹 Automated PDF Export  
- Uses LibreOffice (headless mode)  
- Perfect for enterprise-ready PDF deliverables  
- Graceful fallback when LibreOffice is not available  

### 🔹 Clean Folder Separation  
```
automated-insight-engine/
│── code/       → all source code, CLI, web app, templates
└── outputs/    → all generated PPTX, PDF, charts
```

### 🔹 Web UI for Quick Non-Technical Usage  
- Upload CSV → receive instant downloadable PPTX  
- Flask-powered lightweight UI  
- Perfect for demos & judges  

---

# 🛠 Installation

### 1. Create a virtual environment and install dependencies

#### **Windows (PowerShell)**
```powershell
cd code
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
```

#### **macOS / Linux**
```bash
cd code
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

# 🔑 Optional: Enable AI Insight Generation

Get your OpenAI API key:  
https://platform.openai.com/settings/organization/api-keys

**Windows:**
```powershell
setx OPENAI_API_KEY "sk-your-key-here"
```

**macOS / Linux:**
```bash
export OPENAI_API_KEY="sk-your-key-here"
```

Restart your terminal afterward.

---

# ⚡ Running the Engine (CLI)

### Generate PPTX (with charts + optional LLM)
```bash
python cli.py --input examples/adtech_sample.csv --output report1 --llm
```

Outputs:
```
../outputs/report1.pptx
../outputs/charts/*.png
```

---

### Generate PPTX + PDF
(LibreOffice must be installed)

```bash
python cli.py --input examples/adtech_sample.csv --output exec_report --llm --pdf
```

Outputs:
```
../outputs/exec_report.pptx
../outputs/exec_report.pdf
../outputs/charts/*.png
```

If LibreOffice is missing:
- PPTX still generated  
- PDF conversion skipped safely  

---

# 🌐 Running the Web UI

From inside `code/`:

```bash
python -m web.app
```

Then open:  
**http://127.0.0.1:5000**

Upload a dataset → get a downloadable PPTX report.  
Charts and full HTML responsiveness included.

---

# 📁 Project Structure (Premium Edition)

```
automated-insight-engine/
│
├── code/
│   ├── cli.py
│   ├── requirements.txt
│   ├── README.md
│   │
│   ├── src/
│   │   └── engine/
│   │       ├── ingest.py
│   │       ├── transform.py
│   │       ├── ai.py
│   │       ├── charts.py
│   │       ├── report.py
│   │       └── pdf.py
│   │
│   ├── templates/
│   │   └── ppt_template.pptx   (optional branding)
│   │
│   ├── web/
│   │   ├── app.py
│   │   └── templates/
│   │       └── index.html
│   │
│   └── examples/
│       └── adtech_sample.csv
│
└── outputs/
    ├── *.pptx
    ├── *.pdf
    └── charts/
```

---

# 🧪 Testing

Run all tests from inside the `code/` folder:

```bash
pytest -q
```

---

# 🔄 CI / CD (GitHub Actions)

To enable PDF generation in CI, add:

```yaml
- name: Install LibreOffice
  run: sudo apt-get update && sudo apt-get install -y libreoffice
```

---

# 📄 License  
MIT License
