from copy import Error

import pymupdf
from semantic_text_splitter import TextSplitter


def parse_file_get_chunks(file_path: str):
    try:
        if file_path == "":
            raise Error("File Name is Missing")

        doc = pymupdf.open(file_path)
        all_chunks = []
        # min 200 and max 1000 characters
        splitter = TextSplitter((200, 1000))
        for page_number, page in enumerate(doc):
            page_text = page.get_text()
            page_chunks = splitter.chunks(text=page_text)

            all_chunks.append({"page_number": page_number + 1, "content": page_chunks})

        return all_chunks
    except Exception as e:
        print("Unable to generate chunks:", e)
        raise e
