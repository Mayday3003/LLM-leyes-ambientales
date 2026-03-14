import sys 
from pathlib import Path
from backend.services.ingestion import ExtractTextFromPdf


BASE = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE / "backend"))

RAW_DIR = BASE / "data" / "raw"

def main(): 
    pdfs = list(RAW_DIR.glob("*.pdf"))

    all_docs:list = []

    for pdf_path in pdfs:
        base_name = pdf_path.stem
        print(base_name)
        # pdf_chunk = Algo



if __name__ == "__main__":
    main()


