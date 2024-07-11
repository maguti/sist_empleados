from flask import Flask
from flask import render_template,request
from controller_db import *

app = Flask(__name__)

@app.route('/')
def index():
    empleado = getEmpleadoById(4)
    updEmpleadoById(1,'Juan Perez','jperez@correo.com','unafotodejuan.jpg')
    delEmpleadoById(6)
    empleados = getEmpleados()
    return render_template('empleados/index.html',empleados=empleados, empleado=empleado)

@app.route('/create/')
def create():
    return render_template('empleados/create.html')

@app.route('/store', methods=['POST'])
def storage():
    newEmpleado('Mario Gonzalez', 'mario@live.com', 'mario.jpg')
    return render_template('empleados/index.html',empleados=empleados, empleado=empleado)

if __name__ == '__main__':
    app.run(debug=True)
