import os
import pinecone
from langchain.vectorstores.pinecone import Pinecone
from app.chat.embeddings.openai import embeddings

pinecone.Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"),
    host=os.getenv("PINECONE_HOST"),
    environment = os.getenv("PINECONE_ENV_NAME"),

)

vector_store = Pinecone.from_existing_index(
    os.getenv("PINECONE_INDEX_NAME"), embeddings
)

def build_retriever(chat_args, k):
    search_kwargs = { "filter": {"pdf_id": chat_args.pdf_id}, "k": k }
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )
