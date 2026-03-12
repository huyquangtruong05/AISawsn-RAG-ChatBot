from sentence_transformers import SentenceTransformer

# model embedding
embed_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed_query(query: str):
    """
    Convert user question to embedding vector
    """
    embedding = embed_model.encode([query], normalize_embeddings=True)

    return embedding