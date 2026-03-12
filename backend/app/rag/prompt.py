def build_prompt(question, contexts):

    context_text = "\n\n".join(contexts)

    prompt = f"""
You are an AI assistant.

Use ONLY the context below to answer the question.

Context:
{context_text}

Question:
{question}

Answer:
"""

    return prompt