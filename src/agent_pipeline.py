from src.loader import PDFLoader
from src.chunking import SemanticChunkerService
from src.embeddings import EmbeddingService
from src.vectorstore import VectorStoreService
from src.retrieval import Retriever

from src.llm_agent import RetailAgent

from dotenv import load_dotenv
load_dotenv()

import os
import certifi

os.environ["AWS_CA_BUNDLE"] = certifi.where()

loader = PDFLoader(
    "C:/Users/ssandeep011/Downloads/Semantic RAG Agent for Retail/Data/Retail_Display_Manual.pdf"
)

documents = loader.load()

embeddings = EmbeddingService().get_embeddings()

chunker = SemanticChunkerService(embeddings)

chunks = chunker.create_chunks(
    documents=documents
)


db = VectorStoreService(
    embeddings
).create_db(chunks)


retriever = Retriever(db)

retrieved_docs = retriever.search(
    "What is the required temperature range for the cold vault?"
)

for doc in retrieved_docs:

    print(f"\nPage No : {doc.metadata['page']}")
    print(f"\nRetrieved Document : {doc.page_content}")
    print("-" * 50)

questions = [
    "What are the requirements for seasonal display transitions?",
    "List out few Safety & Compliance Protocols?",
    "Can you explain the Shelf Planogram Guidelines?",
    "What is the full form of BOGO?",
    "What is the required temperature range for the cold vault?"
]


agent = RetailAgent(
    retriever=retriever
)


for i, question in enumerate(questions, 1):

    print(f"\nQuestion {i}: {question}")

    result = agent.ask(question)

    print("\nAgent Answer:")
    print(result["answer"])

    print("-" * 50)

    print("\nMetadata Information - ")

    seen_pages = set()

    for doc in result["documents"]:

        page = doc.metadata.get("page", "N/A")

        if page in seen_pages:
            continue

        seen_pages.add(page)

        print(f"\nPage : {page}")
        print(
            f"Source Path : "
            f"{doc.metadata.get('source', 'N/A')}"
        )
        print(
            f"Heading : "
            f"{doc.metadata.get('heading', 'N/A')}"
        )
        print(
            f"Content Type : "
            f"{doc.metadata.get('content_type', 'N/A')}"
        )
        print(
            f"Length : "
            f"{doc.metadata.get('length', 'N/A')}"
        )

        print("-" * 50)