import os
from typing import List, Dict, Optional
from dotenv import load_dotenv
import openai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader, PyPDFLoader
import json

load_dotenv()


class RAGService:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.embeddings = OpenAIEmbeddings(openai_api_key=self.openai_api_key)
        self.vector_store = None
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
    
    def load_textbook_data(self, subject: str, grade: str) -> None:
        """
        Load textbook data for specific subject and grade
        """
        try:
            # TODO: Load actual textbook data
            # This would typically load from PDF files or database
            textbook_path = f"data/textbooks/{subject}_{grade}.txt"
            
            if os.path.exists(textbook_path):
                with open(textbook_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                
                # Split text into chunks
                chunks = self.text_splitter.split_text(text)
                
                # Create vector store
                self.vector_store = FAISS.from_texts(chunks, self.embeddings)
            else:
                # Create mock data for testing
                mock_text = f"Đây là nội dung sách giáo khoa {subject} lớp {grade}..."
                chunks = self.text_splitter.split_text(mock_text)
                self.vector_store = FAISS.from_texts(chunks, self.embeddings)
                
        except Exception as e:
            print(f"Error loading textbook data: {e}")
    
    def search_relevant_passages(self, query: str, k: int = 5) -> List[Dict]:
        """
        Search for relevant passages in textbook
        """
        if not self.vector_store:
            return []
        
        try:
            docs = self.vector_store.similarity_search(query, k=k)
            results = []
            
            for i, doc in enumerate(docs):
                # Extract page number and chapter info from metadata
                # This would need to be implemented based on actual data structure
                results.append({
                    "content": doc.page_content,
                    "page": i + 1,  # Mock page number
                    "chapter": f"Chương {i + 1}",
                    "relevance_score": 0.9 - (i * 0.1)
                })
            
            return results
        except Exception as e:
            print(f"Error searching passages: {e}")
            return []
    
    def generate_answer_with_citations(self, query: str, subject: str, grade: str) -> Dict:
        """
        Generate answer with citations from textbook
        """
        try:
            # Load textbook data
            self.load_textbook_data(subject, grade)
            
            # Search relevant passages
            passages = self.search_relevant_passages(query)
            
            if not passages:
                return {
                    "answer": "Không tìm thấy thông tin liên quan trong sách giáo khoa.",
                    "citations": [],
                    "confidence_score": 0.0
                }
            
            # Generate answer using OpenAI
            client = openai.OpenAI(api_key=self.openai_api_key)
            
            context = "\n".join([f"Trang {p['page']}: {p['content']}" for p in passages])
            
            prompt = f"""
            Dựa trên thông tin từ sách giáo khoa sau đây, hãy trả lời câu hỏi của học sinh:
            
            Thông tin từ sách giáo khoa:
            {context}
            
            Câu hỏi: {query}
            
            Hãy trả lời một cách rõ ràng, chính xác và có trích dẫn từ sách giáo khoa.
            """
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Bạn là một gia sư AI chuyên nghiệp, trả lời dựa trên sách giáo khoa."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500
            )
            
            answer = response.choices[0].message.content
            
            return {
                "answer": answer,
                "citations": passages,
                "confidence_score": 0.85
            }
            
        except Exception as e:
            print(f"Error generating answer: {e}")
            return {
                "answer": "Có lỗi xảy ra khi xử lý câu hỏi.",
                "citations": [],
                "confidence_score": 0.0
            }

# Global instance
rag_service = RAGService() 