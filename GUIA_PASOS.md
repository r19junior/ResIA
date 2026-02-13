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

Coloca los archivos que deseas analizar en la carpeta `data/`:
- **Bases de Datos:** Copia tus archivos `.db` (SQLite) a `data/`.
- **Libros/Documentos:** Copia tus archivos `.pdf` o `.txt` a `data/`.

## 4. Ejecución del Analizador de DB

Para probar el analizador de bases de datos, abre el archivo `src/db_analyzer.py` y asegúrate de que la ruta a tu base de datos sea correcta, luego ejecútalo:

```bash
python src/db_analyzer.py
```

## Próximos Pasos Sugeridos
- [ ] Implementar el procesador de libros con RAG.
- [ ] Crear el script principal `main.py` para manejar todo desde un solo lugar.
