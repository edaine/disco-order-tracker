# filepath: scripts/merge_pdfs.py
from pathlib import Path

from PyPDF2 import PdfMerger

ROOT = Path(__file__).resolve().parent.parent  # Adjust as needed

merger = PdfMerger()
pdf_folder = ROOT / 'passes/pdf'
pdf_files = sorted([pdf_folder / f for f in pdf_folder.iterdir() if f.suffix == '.pdf'])

for pdf in pdf_files:
    merger.append(pdf)

merger.write(ROOT / 'passes/pdf/all_passes.pdf')
merger.close()