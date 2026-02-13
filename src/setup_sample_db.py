import sqlite3
import os

def create_sample_db():
    db_path = 'data/sample_data.db'
    
    # Asegurarse de que la carpeta data exista
    os.makedirs('data', exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Crear tablas de ejemplo
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE,
        fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio REAL,
        stock INTEGER
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ventas (
        id INTEGER PRIMARY KEY,
        usuario_id INTEGER,
        producto_id INTEGER,
        cantidad INTEGER,
        total REAL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
        FOREIGN KEY (producto_id) REFERENCES productos(id)
    )
    ''')
    
    # Insertar algunos datos
    cursor.executemany('INSERT OR IGNORE INTO usuarios (nombre, email) VALUES (?, ?)', [
        ('Juan Perez', 'juan@example.com'),
        ('Maria Garcia', 'maria@example.com')
    ])
    
    cursor.executemany('INSERT OR IGNORE INTO productos (nombre, precio, stock) VALUES (?, ?, ?)', [
        ('Laptop Pro', 1200.0, 10),
        ('Mouse Wireless', 25.0, 50),
        ('Monitor 4K', 350.0, 15)
    ])
    
    conn.commit()
    conn.close()
    print(f"Base de datos de ejemplo creada en: {db_path}")

if __name__ == "__main__":
    create_sample_db()
