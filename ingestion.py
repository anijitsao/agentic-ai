from pathlib import Path

from src.utils import get_client, get_collection, parse_file_get_chunks


def start_ingestion():
    try:
        CURRENT_DIR = Path(__file__).resolve().parent
        RAG_DIR = f"{CURRENT_DIR}/src/documents"
        RAG_DOCUMENT = "Weather-Based Activity.pdf"
        file_path = f"{RAG_DIR}/{RAG_DOCUMENT}"
        print("current path", file_path)

        generated_chunks = parse_file_get_chunks(file_path=file_path)
        print("generated chunks", generated_chunks)

        chroma_client = get_client("./weather_store")
        collection = get_collection(
            chroma_client=chroma_client, collection_name="weather_n_play"
        )
        print("collection", collection)
    except Exception as e:
        print("Error occurred in Ingestion process", e)


start_ingestion()
