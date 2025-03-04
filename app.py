import os
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de MySQL
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_DATABASE_HOST', 'localhost')  # Se toma del entorno, si no se encuentra se pone 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Asegúrate de poner tu contraseña si es necesaria
app.config['MYSQL_DB'] = 'mydatabase'

mysql = MySQL(app)  # Asegúrate de pasar la app a MySQL()

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/read from database')
def read():
    # Usamos el contexto de Flask para obtener la conexión
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employees")
    row = cur.fetchone()
    result = []
    while row is not None:
        result.append(row[0])  # Aquí puedes acceder a las columnas de la fila
        row = cur.fetchone()

    cur.close()  # No olvides cerrar el cursor después de usarlo
    return ",".join(result)  # Regresar los resultados como una cadena de texto

if __name__ == "__main__":
    app.run(debug=True)  # Habilitamos debug para mayor facilidad en el desarrollo
