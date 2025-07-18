import requests, zipfile, os
from bs4 import BeautifulSoup

BASE_URL = "https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/2023/"
SAVE_DIR = "uspto_zips"
os.makedirs(SAVE_DIR, exist_ok=True)

def download_zip_links():
    page = requests.get(BASE_URL)
    soup = BeautifulSoup(page.text, "html.parser")
    links = [a['href'] for a in soup.find_all('a') if a['href'].endswith('.zip')][:10]  # Limit to ~500 patents

    for link in links:
        zip_url = BASE_URL + link
        print(f"Downloading {zip_url}")
        r = requests.get(zip_url)
        with open(os.path.join(SAVE_DIR, link), 'wb') as f:
            f.write(r.content)

download_zip_links()
