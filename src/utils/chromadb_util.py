import chromadb


def get_client(db_path):
    chroma_client = chromadb.PersistentClient(db_path)
    return chroma_client


def get_collection(chroma_client, collection_name):
    collection = chroma_client.get_or_create_collection(collection_name)
    return collection


def add_items(collection, ids, documents, metadatas):
    collection.add(ids=ids, documents=documents, metadatas=metadatas)


def get_peek_items(collection):
    return collection.peek()


def get_documents(collection, texts, n_results=3):
    return collection.query(query_texts=texts, n_results=n_results)
