import numpy as np
from groq import Groq
import faiss
from sentence_transformers import SentenceTransformer
import os

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Groq model
CHAT_MODEL = "llama-3.3-70b-versatile"

# Local embedding model (free alternative to OpenAI embeddings)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_query(query: str):
    """Embed a single query using sentence-transformers"""
    vec = embedding_model.encode([query], convert_to_numpy=True, normalize_embeddings=True)
    return vec.astype('float32')

def retrieve(query, index, chunks, k=4):
    """Retrieve top-k relevant chunks for the query"""
    qvec = embed_query(query)
    scores, ids = index.search(qvec, k)
    results = []
    for i in ids[0]:
        if i != -1:
            results.append(chunks[i])
    return results

def generate_answer(user_question, retrieved_chunks):
    """Generate answer using Groq's LLM"""
    context = "\n\n".join(retrieved_chunks)

    # Create the prompt for Groq
    system_message = (
        "You are an Insurance Agency Customer Care assistant. "
        "Use only the provided context to answer. "
        "If not found, say you don't have it and offer human support."
    )
    
    user_message = f"Context:\n{context}\n\nQuestion:\n{user_question}"

    # Call Groq API
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7,
        max_tokens=1024,
    )
    
    return response.choices[0].message.content