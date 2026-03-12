from .embedder import embed_query
from .vector_store import search
from .reranker import rerank
from .prompt import build_prompt
from .llm import generate


def rag_answer(question: str):

    # 1 embed question
    query_embedding = embed_query(question)

    # 2 vector search
    docs = search(query_embedding, k=10)

    # 3 rerank
    reranked_docs = rerank(question, docs, top_k=3)

    contexts = [doc["text"] for doc in reranked_docs]

    # 4 build prompt
    prompt = build_prompt(question, contexts)

    # 5 generate answer
    answer = generate(prompt)

    return answer