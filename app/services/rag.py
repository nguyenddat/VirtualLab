import os
from typing import List

import pytesseract
from tqdm import tqdm
from langchain.schema import Document
from pdf2image import convert_from_path
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

from app.core.llm import llm, embeddings
from app.utils.chatbot_utils.state import State
from app.utils.chatbot_utils.chain import get_chat_completion_stream
from app.services.physic_explain import rewrite_graph

class Rag:
    def __init__(self, file_name: str):
        self.save_local = os.path.join(os.getcwd(), "app", "artifacts", "rag")
        os.makedirs(self.save_local, exist_ok=True)

        self.file_name = file_name
        self.llm = llm
        self.embeddings = embeddings
        self.vector_store = None
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        self.load_notebook_data()
    
    def load_notebook_data(self):
        try:
            self.vector_store = FAISS.load_local(self.save_local, self.embeddings, allow_dangerous_deserialization=True)
            print(f"Loaded existing FAISS index from {self.save_local}")
        
        except Exception as e:
            print(f"Could not load existing FAISS index: {e}")
            print("Creating new FAISS index from PDF...")
            
            documents = []
            file_path = os.path.join(os.getcwd(), "app", "static", self.file_name)
            pages = convert_from_path(file_path, dpi=300)
            
            for page_num, page in tqdm(enumerate(pages, start=1), total=len(pages), desc="Processing pages"):
                text = pytesseract.image_to_string(page, lang='vie')
                if text.strip():  # Only add non-empty pages
                    doc = Document(
                        page_content=text,
                        metadata={"page": page_num, "source": self.file_name}
                    )
                    documents.append(doc)
            
            # Split documents while preserving metadata
            chunks = []
            for doc in documents:
                text_chunks = self.text_splitter.split_text(doc.page_content)
                for chunk in text_chunks:
                    chunk_doc = Document(
                        page_content=chunk,
                        metadata=doc.metadata.copy()
                    )
                    chunks.append(chunk_doc)
            
            self.vector_store = FAISS.from_documents(chunks, self.embeddings)
            self.vector_store.save_local(self.save_local)

    def get_k_relevant_chunks(self, query: str, k: int = 5) -> List[Document]:
        docs = self.vector_store.similarity_search(query, k=k)
        context = []
        for doc in docs:
            context.append(f"Trang {doc.metadata['page']} nguồn: {doc.metadata['source']}\n{doc.page_content}")
        return context

    def invoke(self, state: State, k: int = 3):
        docs = self.get_k_relevant_chunks(state.question, k)
        sources = []
        full_response = ""
        
        print("Starting RAG response generation...")
        state = rewrite_graph(state)
        for chunk in get_chat_completion_stream(
            task="rag",
            params={"question": state.question, "context": state.graph, "data": "\n".join(docs)}
        ):
            if isinstance(chunk, str):
                yield chunk
                full_response += chunk
            else:
                yield chunk.response
                full_response += chunk.response
                sources = chunk.citations
        
        yield {
            "response": full_response, 
            "sources": [{
                "summary": s.summary,
                "page": s.page,
                "filename": s.filename
            } for s in sources]
        }