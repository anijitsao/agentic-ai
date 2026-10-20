import chromadb


def get_client():
    chroma_client = chromadb.Client()
    return chroma_client


def get_collection(chroma_client, collection_name):
    collection = chroma_client.get_or_create_collection(collection_name)
    return collection
