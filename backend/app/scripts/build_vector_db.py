import os
import fitz
import faiss
import pickle
import numpy as np
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

# ====================================
# PATH CONFIG
# ====================================

# D:\ai_chatbot\backend\app\scripts
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__)) 

# Lùi ra để lấy thư mục gốc D:\ai_chatbot
APP_DIR = os.path.dirname(CURRENT_DIR)       # \app
BACKEND_DIR = os.path.dirname(APP_DIR)       # \backend
ROOT_DIR = os.path.dirname(BACKEND_DIR)      # \ai_chatbot

# Trỏ chính xác tới thư mục data và vector_db ở root
PDF_FOLDER = os.path.join(ROOT_DIR, "data", "pdf")
VECTOR_DB_FOLDER = os.path.join(APP_DIR, "vector_db")

# ====================================
# PARAMETERS
# ====================================

CHUNK_SIZE = 300
CHUNK_OVERLAP = 50

TOP_K = 5

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# ====================================
# LOAD EMBEDDING MODEL
# ====================================

print("Loading embedding model...")

model = SentenceTransformer(EMBEDDING_MODEL)

# ====================================
# PDF TEXT EXTRACTION
# ====================================

def extract_pdf_pages(file_path):

    pages = []

    try:

        doc = fitz.open(file_path)

        for page_number, page in enumerate(doc):

            text = page.get_text()

            if text.strip():

                pages.append({
                    "page": page_number + 1,
                    "text": text
                })

    except Exception as e:

        print(f"Error reading {file_path}: {e}")

    return pages

# ====================================
# TEXT CHUNKING
# ====================================

def chunk_text(text, chunk_size=300, overlap=50):

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(words[start:end])

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks

# ====================================
# LOAD PDF DOCUMENTS
# ====================================

print("Scanning PDF folder:", PDF_FOLDER)

documents = []
metadata = []

chunk_id = 0

pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith(".pdf")]

for file in tqdm(pdf_files, desc="Processing PDFs"):

    file_path = os.path.join(PDF_FOLDER, file)

    pages = extract_pdf_pages(file_path)

    for page in pages:

        page_number = page["page"]
        text = page["text"]

        chunks = chunk_text(text, CHUNK_SIZE, CHUNK_OVERLAP)

        for chunk in chunks:

            documents.append(chunk)

            metadata.append({
                "chunk_id": chunk_id,
                "source": file,
                "page": page_number
            })

            chunk_id += 1

print("Total chunks created:", len(documents))

# ====================================
# CREATE EMBEDDINGS
# ====================================

print("Generating embeddings...")

embeddings = model.encode(
    documents,
    batch_size=32,
    show_progress_bar=True,
    normalize_embeddings=True
)

embeddings = np.array(embeddings).astype("float32")

# ====================================
# BUILD FAISS INDEX (COSINE SIMILARITY)
# ====================================

print("Building FAISS index...")

dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)

index.add(embeddings)

print("Total vectors indexed:", index.ntotal)

# ====================================
# SAVE VECTOR DATABASE
# ====================================

os.makedirs(VECTOR_DB_FOLDER, exist_ok=True)

faiss_path = os.path.join(VECTOR_DB_FOLDER, "faiss.index")
doc_path = os.path.join(VECTOR_DB_FOLDER, "documents.pkl")
meta_path = os.path.join(VECTOR_DB_FOLDER, "metadata.pkl")

faiss.write_index(index, faiss_path)

with open(doc_path, "wb") as f:
    pickle.dump(documents, f)

with open(meta_path, "wb") as f:
    pickle.dump(metadata, f)

print("\nVector Database successfully created")

print("\nSaved files:")
print(faiss_path)
print(doc_path)
print(meta_path)