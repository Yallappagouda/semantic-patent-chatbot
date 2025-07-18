
# 🧠 Semantic Patent Chatbot  
**Team:** Silo Patent Whisperers  
**Track:** Data Science — SiloFortune Hackathon  
**Challenge:** Deep-Semantic Patent Search Without LLMs

---

## 🚀 Overview

Global patent repositories exceed 160 million filings. Researchers struggle to find relevant paragraphs using keyword search alone. Our chatbot solves this by understanding **semantic meaning**, not just string matches.

Ask:
> “What materials are used in non-flammable insulation foams?”

Get:
> US 2023/0123456 A1 — §[0032]: “A foam composition comprising non-flammable polymeric materials…”

Follow up with:
> “Narrow that to filings after 2020.”

And the bot refines results instantly.

---

## 🎯 Features

- ✅ Semantic search using Sentence-BERT (local-only)
- ✅ No external LLM APIs (fully offline)
- ✅ Multi-turn query refinement
- ✅ Paragraph-level citation with claim IDs
- ✅ Handles ≥500 full-text patents
- ✅ Fast response via FAISS vector search

---

## 🧱 Architecture

```
USPTO ZIPs → XML Parser → JSON Corpus → Sentence-BERT → FAISS Index → Flask Chatbot
```

- **Data Source**: USPTO Bulk Data (manual ZIP download)
- **Embedding Model**: `all-MiniLM-L6-v2` via Hugging Face
- **Vector Store**: FAISS
- **Backend**: Flask
- **Frontend**: Minimal HTML (optional)

---

## 📦 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/<your-username>/semantic-patent-chatbot.git
cd semantic-patent-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download USPTO ZIPs Manually

Go to [USPTO Bulk Data](https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/2023/)  
Download 5–10 ZIPs and place them in:

```
data/raw_zips/
```

### 5. Run the Pipeline

```bash
python scripts/parse_patents.py
python scripts/embed_patents.py
python chatbot/app.py
```

---

## 🔍 Query Example

```bash
curl -X POST http://127.0.0.1:5000/query ^
-H "Content-Type: application/json" ^
-d "{\"query\": \"rice-based edible straws\"}"
```

### Sample Output

```json
[
  {
    "patent_id": "US20230123456A1",
    "section": "claim_3",
    "text": "A consumable drinking tube formed by extrusion of rice-flour starch...",
    "citation": "US20230123456A1 — §[claim_3]: A consumable drinking tube formed by extrusion..."
  }
]
```

---

## 📁 Project Structure

```
semantic-patent-chatbot/
├── data/
│   ├── raw_zips/
│   ├── json_patents/
│   ├── patent_index.faiss
│   └── metadata.json
├── scripts/
│   ├── parse_patents.py
│   ├── embed_patents.py
├── chatbot/
│   ├── app.py
│   ├── query_handler.py
│   └── utils.py
├── ui/
│   └── index.html
├── requirements.txt
└── README.md
```

---

