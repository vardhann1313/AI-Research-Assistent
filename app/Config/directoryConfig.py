import os

# Upload directory for file
UPLOAD_DIR = os.path.join(os.getcwd(), "Uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Upload directory for chromaDB
CHROMA_DIR = os.path.join(os.getcwd(), "ChromaDB")
os.makedirs(CHROMA_DIR, exist_ok=True)