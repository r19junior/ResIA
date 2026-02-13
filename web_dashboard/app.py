from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from logic.processor_bridge import ProcessorBridge

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB

# Asegurar que la carpeta de uploads exista
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

bridge = ProcessorBridge()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if 'file' not in request.files:
        return jsonify({'error': 'No se seleccionó ningún archivo'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nombre de archivo vacío'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    print(f"DEBUG: Archivo guardado en {file_path}")

    # Llamar al puente de lógica
    print(f"DEBUG: Iniciando resumen para {filename}")
    summary = bridge.get_summary_from_file(file_path)
    print(f"DEBUG: Resumen completado para {filename}")
    
    return jsonify({'summary': summary})

@app.route('/analyze-db', methods=['POST'])
def analyze_db():
    data = request.json
    db_url = data.get('db_url')
    if not db_url:
        return jsonify({'error': 'Se requiere una URL de base de datos'}), 400

    summary = bridge.get_db_summary(db_url)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    print("Iniciando Dashboard Inteligente en http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
