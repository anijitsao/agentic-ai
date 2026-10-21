import os
from pathlib import Path

from dotenv import load_dotenv

from src.tools import fetch_activities
from src.utils import (
    add_items,
    get_client,
    get_collection,
    get_documents,
    parse_file_get_chunks,
)

load_dotenv()


def insert_chunks_to_vector_db(generated_chunks):
    chroma_client = get_client(f"./{os.getenv('CHROMA_DB_NAME')}")
    collection = get_collection(
        chroma_client=chroma_client, collection_name=os.getenv("CHROMA_DB_COLLECTION")
    )
    ids = [f"chunk_{i + 1}" for i in range(len(generated_chunks))]
    documents = [",".join(doc["content"]) for doc in generated_chunks]
    metadatas = [{"page": doc["page_number"]} for doc in generated_chunks]

    add_items(collection=collection, ids=ids, documents=documents, metadatas=metadatas)


def start_ingestion():
    try:
        CURRENT_DIR = Path(__file__).resolve().parent
        RAG_DIR = f"{CURRENT_DIR}/src/documents"
        RAG_DOCUMENT = "Weather-Based Activity.pdf"
        file_path = f"{RAG_DIR}/{RAG_DOCUMENT}"
        print("current path", file_path)

        generated_chunks = parse_file_get_chunks(file_path=file_path)
        insert_chunks_to_vector_db(generated_chunks=generated_chunks)
    except Exception as e:
        print("Error occurred in Ingestion process", e)


start_ingestion()
fetch_activities(["sunny day", "temperature 18C"])
