# nodes/extract_content.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from vector_store import store_content

def extract_content(state):
    url = state["url"]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    headings = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])]
    paragraphs = [p.get_text(strip=True) for p in soup.find_all('p') if len(p.get_text(strip=True)) > 40]

    content = {
        "headings": headings,
        "paragraphs": paragraphs
    }

    # ✅ Store in ChromaDB
    store_content(content, url)

    return {
        "url": url,
        "content": content
    }
