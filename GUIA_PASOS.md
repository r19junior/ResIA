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

## 4. Ejecución del Analizador de DB (PostgreSQL)

Para probar el analizador, abre `src/db_analyzer.py` y configura tu URL de conexión:

```python
# Formato: postgresql://usuario:password@host:puerto/nombre_db
db_url = "postgresql://postgres:mi_password@localhost:5432/mi_base_de_datos"
analyzer = LlamaDBAnalyzer(db_url)
print(analyzer.summarize_db())
```

Luego ejecútalo:
```bash
python src/db_analyzer.py
```

## Próximos Pasos Sugeridos
- [ ] Implementar el procesador de libros con RAG.
- [ ] Crear el script principal `main.py` para manejar todo desde un solo lugar.
