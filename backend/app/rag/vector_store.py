import os
import faiss
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
VECTOR_DB_PATH = os.path.join(BASE_DIR, "vector_db")

# load index
index = faiss.read_index(os.path.join(VECTOR_DB_PATH, "faiss.index"))

# load documents
with open(os.path.join(VECTOR_DB_PATH, "documents.pkl"), "rb") as f:
    documents = pickle.load(f)

# load metadata
with open(os.path.join(VECTOR_DB_PATH, "metadata.pkl"), "rb") as f:
    metadata = pickle.load(f)


def search(query_embedding, k=10):
    """
    Search FAISS vector DB
    """
    scores, indices = index.search(query_embedding, k)

    results = []

    for i in indices[0]:
        results.append({
            "text": documents[i],
            "metadata": metadata[i]
        })

    return results