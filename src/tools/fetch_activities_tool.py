import os

from agents.decorators import tool

from src.utils import get_client, get_collection, get_documents


@tool
def fetch_activities(keywords):
    chroma_client = get_client(f"./{os.getenv('CHROMA_DB_NAME')}")
    collection = get_collection(
        chroma_client=chroma_client, collection_name=os.getenv("CHROMA_DB_COLLECTION")
    )
    documents = get_documents(
        collection,
        keywords,
    )
    print("documents", documents)
    return documents
