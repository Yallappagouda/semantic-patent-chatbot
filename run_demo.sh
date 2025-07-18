#!/bin/bash
echo "Running full pipeline..."
python scripts/scrape_uspto.py
python scripts/parse_patents.py
python scripts/embed_patents.py
python chatbot/app.py
