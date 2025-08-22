from langchain.vectorstores import FAISS 
from langchain.embeddings import HuggingFaceEmbeddings 

def get_vectorstore():
    # HuggingFace embeddings (free)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    # Local in-memory FAISS vector DB
    vs = FAISS(embedding_function=embeddings)
    return vs

