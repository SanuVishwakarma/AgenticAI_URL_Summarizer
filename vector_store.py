# vector_store.py
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embedding_model)

def store_content(content, url):
    docs = [Document(page_content=text, metadata={"source": url})
            for text in content['headings'] + content['paragraphs']]
    vectorstore.add_documents(docs)
