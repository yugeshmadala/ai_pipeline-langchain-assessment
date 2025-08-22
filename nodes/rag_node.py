from utils.vectorstore import get_vectorstore
from utils.pdf_loader import load_pdf

# Load and store the PDF into FAISS on first call
_vectorstore = None
def init_vectorstore(pdf_path="data/sample_data.pdf"):
    global _vectorstore
    docs = load_pdf(pdf_path)
    vs = get_vectorstore()
    vs.add_documents(docs)
    _vectorstore = vs

def rag_query(query: str):
    if _vectorstore is None:
        init_vectorstore()
    docs = _vectorstore.similarity_search(query, k=3)
    return "\n".join([d.page_content for d in docs])