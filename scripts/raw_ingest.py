import os
import json
from langchain.document_loaders import CSVLoader, PyPDFLoader

def ingest():
    docs = []
    docs += CSVLoader(file_path="data/sales_hessen.csv").load()
    docs += PyPDFLoader(file_path="data/zoning_hessen.pdf").load()
    docs += CSVLoader(file_path="data/transit_hessen.csv").load()
    with open("data/market_trends_hessen.json", "r") as f:
        docs.append({"page_content": f.read(), "metadata": {"source": "market_trends"}})
    with open("data/schools_hessen.geojson", "r") as f:
        docs.append({"page_content": f.read(), "metadata": {"source": "schools_geojson"}})
    return docs