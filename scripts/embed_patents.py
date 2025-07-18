from sentence_transformers import SentenceTransformer
import json, os
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
JSON_DIR = "patent_json"
INDEX_FILE = "patent_index.faiss"
METADATA_FILE = "metadata.json"

texts, metadata = [], []

for file in os.listdir(JSON_DIR):
    with open(os.path.join(JSON_DIR, file)) as f:
        data = json.load(f)
        for i, claim in enumerate(data["claims"]):
            texts.append(claim)
            metadata.append({
                "patent_id": data["patent_id"],
                "section": f"claim_{i}",
                "text": claim
            })

embeddings = model.encode(texts, show_progress_bar=True)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

faiss.write_index(index, INDEX_FILE)
with open(METADATA_FILE, "w") as f:
    json.dump(metadata, f, indent=2)
