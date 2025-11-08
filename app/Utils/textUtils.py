import os
from pypdf import PdfReader
import docx2txt

def extract_text(file_path: str, ext: str) -> str:
    
    """
    Extracts text content from PDF, DOCX, or TXT files.
    Returns plain text as a single string.
    """
    text = ""

    try:
        if ext == ".pdf":
            with open(file_path, "rb") as f:
                reader = PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text() or ""

        elif ext == ".docx":
            text = docx2txt.process(file_path)

        elif ext in [".txt", ".md"]:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()

        else:
            raise ValueError(f"Unsupported file format: {ext}")

    except Exception as e:
        raise Exception(f"Failed to extract text from {file_path}: {str(e)}")

    return text

