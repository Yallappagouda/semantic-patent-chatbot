import zipfile, os, xml.etree.ElementTree as ET, json
from tqdm import tqdm

ZIP_DIR = "uspto_zips"
JSON_DIR = "patent_json"
os.makedirs(JSON_DIR, exist_ok=True)

def extract_patents(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if file.endswith(".xml"):
                zip_ref.extract(file, "temp")
                tree = ET.parse(os.path.join("temp", file))
                root = tree.getroot()

                patent_id = root.findtext(".//publication-reference//doc-number")
                title = root.findtext(".//invention-title")
                abstract = root.findtext(".//abstract")
                claims = [c.text for c in root.findall(".//claim-text")]
                pub_date = root.findtext(".//publication-reference//date")

                data = {
                    "patent_id": patent_id,
                    "title": title,
                    "abstract": abstract,
                    "claims": claims,
                    "publication_date": pub_date
                }

                with open(f"{JSON_DIR}/{patent_id}.json", "w") as f:
                    json.dump(data, f, indent=2)

for zip_file in tqdm(os.listdir(ZIP_DIR)):
    extract_patents(os.path.join(ZIP_DIR, zip_file))
