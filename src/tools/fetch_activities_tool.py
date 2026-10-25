import os

from agents.decorators import tool

from src.utils import get_client, get_collection, get_documents


@tool
def fetch_activities(
    apparent_temperature: float, wind_speed: float, is_day: float, precipitation: float
):
    chroma_client = get_client(f"./{os.getenv('CHROMA_DB_NAME')}")
    collection = get_collection(
        chroma_client=chroma_client, collection_name=os.getenv("CHROMA_DB_COLLECTION")
    )
    result = get_documents(
        collection,
        [
            f"apparent temperature {apparent_temperature}",
            f"precipitation {precipitation}",
            f"is day {bool(is_day)}",
            f"wind speed {wind_speed}",
        ],
    )
    documents = result.get("documents")[0]
    documents = "\n\n".join(documents)
    if not documents:
        return "No relevant game guidelines found."

    return documents
