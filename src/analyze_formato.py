from book_processor import LlamaBookProcessor
import os

def run_analysis():
    # Ruta al archivo proporcionado por el usuario
    data_file = 'data/Formato.txt'
    
    if not os.path.exists(data_file):
        print(f"Error: No se encontró el archivo {data_file}")
        return

    print(f"Iniciando análisis inteligente de {data_file}...")
    processor = LlamaBookProcessor()
    
    # Obtener el resumen/análisis de Llama 3.1
    result = processor.summarize_large_text(data_file)
    
    print("\n" + "="*50)
    print("RESULTADOS DEL ANÁLISIS DE DATOS")
    print("="*50)
    print(result)
    print("="*50)

    # Guardar resultado
    output_path = 'data/Análisis_Transacciones.txt'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"\nResultado guardado en: {output_path}")

if __name__ == "__main__":
    run_analysis()
