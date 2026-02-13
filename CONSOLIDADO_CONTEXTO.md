# CONTEXTO CONSOLIDADO: Proyecto Llama Data Intelligence

Este documento contiene la totalidad del proyecto actual para ser transferido a otra ventana de contexto.

---

## 1. RESUMEN DEL PROYECTO
Sistema local y gratuito para el análisis de inteligencia y resumen de grandes volúmenes de datos (Bases de Datos PostgreSQL/SQLite y Libros/Documentos extensos) utilizando **Llama 3.1** via Ollama.

## 2. ESTRUCTURA DE ARCHIVOS
- `config/Modelfile`: Configuración de ventana de contexto (128k).
- `data/`: Carpeta para archivos de entrada (.pdf, .txt, .db).
- `src/db_analyzer.py`: Analizador de esquemas y datos de DB.
- `src/book_processor.py`: Procesador de textos largos y libros.
- `requirements.txt`: Dependencias de Python.
- `GUIA_PASOS.md`: Manual de usuario.

---

## 3. CONFIGURACIÓN (config/Modelfile)
```dockerfile
FROM llama3.1
PARAMETER num_ctx 131072
```

---

## 4. DEPENDENCIAS (requirements.txt)
```text
ollama
sqlalchemy
langchain
langchain-community
langchain-ollama
chromadb
pypdf
psycopg2-binary
```

---

## 5. CÓDIGO: ANALIZADOR DE DB (src/db_analyzer.py)
```python
import ollama
from sqlalchemy import create_engine, inspect

class LlamaDBAnalyzer:
    def __init__(self, db_url, model='llama3.1-128k'):
        self.engine = create_engine(db_url)
        self.model = model

    def get_schema(self):
        inspector = inspect(self.engine)
        schema_info = ""
        for table_name in inspector.get_table_names():
            schema_info += f"\nTable: {table_name}\n"
            for column in inspector.get_columns(table_name):
                schema_info += f"  - {column['name']} ({column['type']})\n"
        return schema_info

    def summarize_db(self):
        schema = self.get_schema()
        prompt = f"Basado en el siguiente esquema de base de datos, genera un resumen de qué trata el sistema y cuáles son las entidades principales:\n\n{schema}"
        
        response = ollama.chat(
            model=self.model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']

if __name__ == "__main__":
    # Formato local: sqlite:///data/mi_db.db
    # Formato Postgres: postgresql://usuario:password@localhost:5432/nombre_db
    print("Módulo DB Analyzer cargado y listo para PostgreSQL.")
```

---

## 6. CÓDIGO: PROCESADOR DE LIBROS (src/book_processor.py)
```python
import ollama
import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

class LlamaBookProcessor:
    def __init__(self, model='llama3.1-128k'):
        self.model = model
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)

    def summarize_large_text(self, file_path):
        if not os.path.exists(file_path): return "Error: Archivo no encontrado."
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        prompt = f"Resume el siguiente texto de manera exhaustiva:\n\n{content}"
        response = ollama.chat(model=self.model, messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']

if __name__ == "__main__":
    print("Módulo Book Processor cargado. Listo para resumir textos grandes.")
```

---

## 7. GUÍA DE PASOS RÁPIDOS
1. **Instalar Ollama:** Descargar de ollama.com (Importante: El comando `ollama` falló previamente, asegurar que esté instalado y en el PATH).
2. **Setup Python:** `pip install -r requirements.txt`.
3. **Crear Modelo:** `ollama create llama3.1-128k -f config/Modelfile`.
4. **Ejecutar:** Configura las rutas en los scripts de `src/` y corre con `python src/nombre_script.py`.

---

## 8. INVESTIGACIÓN Y ESTRATEGIAS
- **Bases de Datos:** Se usa extracción de metadatos para evitar saturar el contexto con datos crudos.
- **Libros > 1M tokens:** Implementar **RAG** (Retrieval Augmented Generation) dividiendo el libro en fragmentos vectorizados.
- **Hardware:** Llama 3.1 8B requiere ~8-12GB VRAM para el contexto de 128k.
