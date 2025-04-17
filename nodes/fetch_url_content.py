import requests
from bs4 import BeautifulSoup

def fetch_url_content(state):
    url = state["url"]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return {"url": url, "content": {"html": soup.prettify()}}