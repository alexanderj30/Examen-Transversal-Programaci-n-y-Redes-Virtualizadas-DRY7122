# app_web_hash.py

from flask import Flask, request, render_template_string
import sqlite3
import bcrypt

app = Flask(__name__)
DATABASE = 'usuarios.db'

# Crea tabla si no existe
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Página HTML con formulario
HTML = '''
<h2>Registro de usuarios</h2>
<form method="POST">
  Nombre: <input type="text" name="nombre"><br>
  Contraseña: <input type="password" name="password"><br>
  <input type="submit" value="Registrar">
</form>
'''

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password'].encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, password_hash) VALUES (?, ?)", (nombre, hashed))
        conn.commit()
        conn.close()
        return f"<p>Usuario <b>{nombre}</b> registrado correctamente con contraseña en hash.</p>" + HTML
    return HTML

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=7500)
