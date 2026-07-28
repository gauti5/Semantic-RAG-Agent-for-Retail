
from langchain_chroma import Chroma
from langchain_community.vectorstores.utils import filter_complex_metadata


import shutil
shutil.rmtree("db", ignore_errors=True)


class VectorStoreService:
    def __init__(self, embeddings):
        self.embeddings=embeddings
        
    def create_db(self, chunks):
        chunks = filter_complex_metadata(chunks)
        db=Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory='db'
        )
        print("\nVector Database Created!!")
        return db
    