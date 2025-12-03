import os
import subprocess
from pathlib import Path

# Hardcoded path to LibreOffice for Windows
LIBREOFFICE_PATH = r"C:\Program Files\LibreOffice\program\soffice.exe"

def libreoffice_installed() -> bool:
    """
    Check if LibreOffice exists at the known Windows install path.
    Ignores PATH since some Windows setups block PATH resolution.
    """
    return os.path.exists(LIBREOFFICE_PATH)

def convert_pptx_to_pdf(input_pptx: str, output_pdf: str) -> bool:
    """
    Convert PPTX → PDF using LibreOffice headless mode.
    Uses hardcoded soffice.exe path so PATH problems do not matter.
    """

    if not libreoffice_installed():
        print(f"[WARN] LibreOffice was not found at: {LIBREOFFICE_PATH}")
        print("[WARN] PDF export skipped.")
        return False

    out_dir = str(Path(output_pdf).parent)
    os.makedirs(out_dir, exist_ok=True)

    try:
        subprocess.run(
            [
                LIBREOFFICE_PATH,
                "--headless",
                "--convert-to", "pdf",
                input_pptx,
                "--outdir", out_dir
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        print(f"[INFO] PDF generated: {output_pdf}")
        return True

    except Exception as e:
        print(f"[ERROR] PDF conversion failed: {e}")
        return False
