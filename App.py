import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
import streamlit as st
from typing import Iterable

# Web crawling and Indexing
def crawl(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    content = soup.get_text()
    return {'url': url, 'title': title, 'content': content}

# Search Engine Implementation
class SearchEngine:
    def __init__(self, index):
        self.index = index
    
    def search(self, query):
        # Placeholder search function
        return [item for item in self.index.values() if query.lower() in item['title'].lower()]

# Groq Integration
app = FastAPI()
index = {}  # Placeholder index
search_engine = SearchEngine(index)

@app.get("/search/")
async def search(query: str):
    results = search_engine.search(query)
    return results

# Streamlit UI
st.title("Custom Search Engine")

query = st.text_input("Enter your query:")
if st.button("Search"):
    response = requests.get("http://localhost:8000/search/", params={"query": query})
    results = response.json()
    for result in results:
        st.write(result['title'])
        st.write(result['url'])
