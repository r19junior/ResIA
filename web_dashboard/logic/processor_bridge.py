import sys
import os

# Añadir el directorio raíz al path para poder importar desde src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.book_processor import LlamaBookProcessor
from src.db_analyzer import LlamaDBAnalyzer

class ProcessorBridge:
    def __init__(self):
        self.text_processor = LlamaBookProcessor()
    
    def get_summary_from_file(self, file_path):
        """Puente para resumir archivos subidos."""
        try:
            return self.text_processor.summarize_large_text(file_path)
        except Exception as e:
            return f"Error procesando el archivo: {str(e)}"

    def get_db_summary(self, db_url):
        """Puente para analizar bases de datos."""
        try:
            analyzer = LlamaDBAnalyzer(db_url)
            return analyzer.summarize_db()
        except Exception as e:
            return f"Error analizando la base de datos: {str(e)}"
