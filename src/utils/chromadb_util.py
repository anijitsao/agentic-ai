import chromadb


def get_client(db_path):
    chroma_client = chromadb.PersistentClient(db_path)
    return chroma_client


def get_collection(chroma_client, collection_name):
    collection = chroma_client.get_or_create_collection(collection_name)
    return collection
