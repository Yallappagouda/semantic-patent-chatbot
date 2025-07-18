from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json
from chatbot.utils import format_result

# Load model and index
model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("data/patent_index.faiss")

# Load metadata
with open("data/metadata.json") as f:
    metadata = json.load(f)

def handle_query(user_input, top_k=5):
    query_embedding = model.encode([user_input])
    D, I = index.search(np.array(query_embedding), k=top_k)

    results = []
    for idx in I[0]:
        result = metadata[idx]
        formatted = format_result(result)
        results.append(formatted)

    return results
