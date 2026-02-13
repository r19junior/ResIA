# Guía de Inicio: Proyecto Llama Data Intelligence

Sigue estos pasos para configurar y ejecutar tu sistema de inteligencia de datos local.

## 1. Instalación de Dependencias

Asegúrate de tener Python instalado y ejecuta el siguiente comando en tu terminal para instalar las librerías necesarias:

```bash
pip install -r requirements.txt
```

## 2. Configuración de Llama 3.1 (Ollama)

Para procesar registros y libros extensos, necesitamos configurar una ventana de contexto de **128k tokens**.

> [!TIP]
> **Sobre el error "Only one usage of each socket address":**
> Si ves este error al intentar correr `ollama serve`, es una excelente noticia: significa que **Ollama ya se está ejecutando** en segundo plano (probablemente se inició automáticamente al encender tu PC). No necesitas correr `serve`, puedes ir directo a crear el modelo.

1. Abre una terminal (mejor si es como Administrador).
2. Ejecuta el comando de creación usando la **ruta completa** del ejecutable:
   ```powershell
   & "C:\Users\Lenovo\AppData\Local\Programs\Ollama\ollama.exe" create llama3.1-128k -f config/Modelfile
   ```
3. Verifica que el modelo se haya creado correctamente:
   ```powershell
   & "C:\Users\Lenovo\AppData\Local\Programs\Ollama\ollama.exe" list
   ```
   Deberías ver `llama3.1-128k` en la lista.

## 3. Preparación de Datos

Coloca los archivos que deseas analizar o configura tus conexiones:
- **Bases de Datos (PostgreSQL):** No necesitas copiar archivos. Asegúrate de tener las credenciales (Host, Usuario, Password, DB Name).
- **Base de Datos de Prueba (SQLite):** Si aún no tienes una base de datos propia, puedes crear una de ejemplo ejecutando:
  ```bash
  python src/setup_sample_db.py
  ```
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

## 5. Ejecución del Analizador de DB (SQLite/PostgreSQL)

Para probar el analizador con la base de datos de ejemplo (SQLite):
1. Asegúrate de haber corrido `python src/setup_sample_db.py`.
2. En `src/db_analyzer.py`, asegúrate de que la URL sea:
   ```python
   db_url = "sqlite:///data/sample_data.db"
   ```
3. Alternativamente, para PostgreSQL, usa tu URL:
   ```python
   # Formato: postgresql://usuario:password@host:puerto/nombre_db
   db_url = "postgresql://postgres:mi_password@localhost:5432/mi_base_de_datos"
   ```
4. Ejecútalo:
```bash
python src/db_analyzer.py
```

## 6. Verificación de Hardware (Recomendación)

Al usar el modelo de **128k**, el consumo de memoria de tu tarjeta de video (VRAM) o memoria RAM aumentará significativamente cuando cargues documentos muy largos.

**Si el sistema se bloquea o es muy lento:**
* Reduce el tamaño de los fragmentos en `src/book_processor.py` (`chunk_size`).
* O reduce el `num_ctx` en tu `Modelfile` (ej. de 131072 a 65536) y vuelve a ejecutar el comando `create`.

---
¡El motor está listo! Ahora puedes proceder con tus análisis reales.
