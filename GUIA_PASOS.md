# Guía de Inicio: Proyecto Llama Data Intelligence

Sigue estos pasos para configurar y ejecutar tu sistema de inteligencia de datos local.

## 1. Instalación de Dependencias

Asegúrate de tener Python instalado y ejecuta el siguiente comando en tu terminal para instalar las librerías necesarias:

```bash
pip install -r requirements.txt
```

## 2. Configuración de Llama 3.1 (Ollama)

Para procesar registros y libros extensos, necesitamos configurar una ventana de contexto de **128k tokens**.

1. Abre una terminal.
2. Ejecuta el comando para crear el modelo personalizado:
   ```bash
   ollama create llama3.1-128k -f config/Modelfile
   ```

## 3. Preparación de Datos

Coloca los archivos que deseas analizar o configura tus conexiones:
- **Bases de Datos (PostgreSQL):** No necesitas copiar archivos. Asegúrate de tener las credenciales (Host, Usuario, Password, DB Name).
- **Libros/Documentos:** Copia tus archivos `.pdf` o `.txt` a `data/`.

## 4. Ejecución del Procesador de Textos Grandes (Libros)

Para resumir un texto largo o libro:
1. Coloca tu archivo (ej. `mi_libro.txt`) en la carpeta `data/`.
2. Abre `src/book_processor.py` y configura la ruta:
   ```python
   processor = LlamaBookProcessor()
   print(processor.summarize_large_text('data/mi_libro.txt'))
   ```
3. Ejecútalo:
   ```bash
   python src/book_processor.py
   ```

## 5. Ejecución del Analizador de DB (PostgreSQL)
... (continúa igual)

## Próximos Pasos Sugeridos
- [ ] Implementar el procesador de libros con RAG.
- [ ] Crear el script principal `main.py` para manejar todo desde un solo lugar.
