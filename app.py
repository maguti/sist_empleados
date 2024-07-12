from flask import Flask
from flask import render_template,request,redirect
from controller_db import *

app = Flask(__name__)

@app.route('/')
def index():
    # empleado = getEmpleadoById(4)
    # updEmpleadoById(1,'Juan Perez','jperez@correo.com','unafotodejuan.jpg')
    # delEmpleadoById(6)
    empleados = getEmpleados()
    return render_template('empleados/index.html',empleados=empleados)

@app.route('/create_empl/')
def create_empl():
    title = 'Cargar Nuevo Empleado'
    return render_template('empleados/create_empl.html', title = title)

@app.route('/new_empl', methods=['POST'])
def new_empl():
    nombre = request.form['txtNombre']
    correo = request.form['txtCorreo']
    foto = request.form['txtFoto']
    newEmpleado(nombre=nombre, correo=correo, foto=foto)
    return redirect("/")

@app.route('/edit_empl/<int:id>')
def edit_empl(id):
    title = 'Modificar Empleado'
    empleado = getEmpleadoById(id)
    return render_template('empleados/edit_empl.html', title = title, empleado=empleado)

@app.route('/upd_empl', methods=['POST'])
def upd_empl():
    idempleado = request.form['txtId']
    nombre = request.form['txtNombre']
    correo = request.form['txtCorreo']
    foto = request.form['txtFoto']
    updEmpleadoById(idempleado=idempleado,nombre=nombre, correo=correo, foto=foto)
    return redirect("/")

@app.route('/del_empl/<int:id>')
def del_empl(id):
    delEmpleadoById(id)
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
