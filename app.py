import os
from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de MySQL

app.config['MYSQL_HOST'] = os.environ.get('MYSQL_DATABASE_HOST', 'localhost')
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mydatabase'

mysql = MySQL(app)


#Rutas de la Aplicación


@app.route("/")
def home():
    """Página de inicio"""
    return render_template("index.html")  # Renderiza la plantilla HTML

@app.route("/empleados")
def read():
    """Consulta la base de datos y muestra los empleados en una tabla HTML"""
    try:
        conn = mysql.connection
        cursor = conn.cursor()

        cursor.execute("SELECT id, name FROM employees")  # Asegúrate de que la tabla 'employees' existe
        rows = cursor.fetchall()

        cursor.close()
        return render_template("empleados.html", employees=rows)  # Enviar datos a la plantilla HTML

    except Exception as e:
        return render_template("error.html", error=str(e))  # Página de error si hay problemas



#Iniciar Servidor


if __name__ == "__main__":
    app.run(debug=True)
