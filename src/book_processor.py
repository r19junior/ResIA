import ollama
import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

class LlamaBookProcessor:
    def __init__(self, model='llama3.1-128k'):
        self.model = model
        self.embeddings = OllamaEmbeddings(model=model)
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200
        )

    def process_file(self, file_path):
        """Carga y divide el archivo en fragmentos."""
        if file_path.endswith('.pdf'):
            loader = PyPDFLoader(file_path)
        else:
            loader = TextLoader(file_path, encoding='utf-8')
        
        docs = loader.load()
        return self.text_splitter.split_documents(docs)

    def summarize_large_text(self, file_path):
        """
        Resumen para textos que caben en la ventana de 128k.
        Para textos más grandes, se debe usar RAG (pendiente integración).
        """
        if not os.path.exists(file_path):
            return "Error: El archivo no existe."

        # Prompt especializado si parece ser un log de datos
        if "ID_TRANSACCION" in content or "|" in content:
            prompt = (
                "Analiza el siguiente registro de transacciones. Proporciona:\n"
                "1. Un resumen ejecutivo del volumen de ventas.\n"
                "2. Los 3 productos más vendidos.\n"
                "3. La región con mayor actividad.\n"
                "4. Cualquier anomalía o tendencia notable (ej. métodos de pago preferidos).\n\n"
                f"Datos:\n{content}"
            )
        else:
            prompt = f"Resume el siguiente texto de manera exhaustiva, destacando los puntos clave y conclusiones:\n\n{content}"
        
        response = ollama.chat(
            model=self.model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']

if __name__ == "__main__":
    # Ejemplo de uso
    # processor = LlamaBookProcessor()
    # print(processor.summarize_large_text('data/libro.txt'))
    print("Módulo Book Processor cargado. Listo para resumir textos grandes.")
