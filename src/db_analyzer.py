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
    # Ejemplo con PostgreSQL
    # db_url = "postgresql://usuario:password@localhost:5432/mi_base_de_datos"
    # analyzer = LlamaDBAnalyzer(db_url)
    # print(analyzer.summarize_db())
    print("Módulo DB Analyzer cargado y listo para PostgreSQL.")
