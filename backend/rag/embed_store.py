import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Local embedding model (free alternative to OpenAI embeddings)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_texts(texts):
    """Embed multiple texts using sentence-transformers"""
    vectors = embedding_model.encode(
        texts, 
        convert_to_numpy=True, 
        normalize_embeddings=True,
        show_progress_bar=True
    )
    return vectors.astype('float32')

def build_and_save_index(chunks, index_path, meta_path):
    """Build FAISS index and save it along with chunk metadata"""
    vectors = embed_texts(chunks)
    dim = vectors.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(vectors)

    faiss.write_index(index, index_path)
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump({"chunks": chunks}, f, ensure_ascii=False, indent=2)

def load_index(index_path, meta_path):
    """Load FAISS index and chunk metadata"""
    index = faiss.read_index(index_path)
    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)
    return index, meta["chunks"]