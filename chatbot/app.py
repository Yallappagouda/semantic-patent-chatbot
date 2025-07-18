from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
import faiss, json, numpy as np

app = Flask(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("patent_index.faiss")

with open("metadata.json") as f:
    metadata = json.load(f)

@app.route("/query", methods=["POST"])
def query():
    user_input = request.json["query"]
    embedding = model.encode([user_input])
    D, I = index.search(np.array(embedding), k=5)

    results = []
    for idx in I[0]:
        results.append(metadata[idx])

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
