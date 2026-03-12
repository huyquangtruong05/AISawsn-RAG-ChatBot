from sentence_transformers import CrossEncoder

reranker_model = CrossEncoder("BAAI/bge-reranker-base")


def rerank(question, docs, top_k=3):
    """
    Rerank documents based on relevance
    """

    texts = [doc["text"] for doc in docs]

    pairs = [[question, text] for text in texts]

    scores = reranker_model.predict(pairs)

    scored_docs = list(zip(scores, docs))

    scored_docs.sort(key=lambda x: x[0], reverse=True)

    reranked = [doc for score, doc in scored_docs[:top_k]]

    return reranked