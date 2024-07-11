import pymysql
from db import conectarMySQL

# CRUD -> Create, Read, Update, Delete 

# Read -> SELECT 1) Leer todos
def getEmpleados():
    # conexion mysql
    conexion = conectarMySQL()
    result = []
    with conexion.cursor() as cursor:
        # Create a new record
        sql = """SELECT * FROM empleados"""
        cursor.execute(sql)
        result = cursor.fetchall()
        conexion.commit()
        conexion.close()
        return result
    
# Read 2) Leer solo uno
def getEmpleadoById(id):
    conexion = conectarMySQL()
    result = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM empleados WHERE idempleado = %s", (id,))
        result = cursor.fetchone()
    conexion.close()
    return result

# Create -> Insert
def newEmpleado(nombre, correo, foto):
    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        sql = "INSERT INTO empleados (nombre, correo, foto) VALUES (%s, %s, %s)"
        cursor.execute(sql,(nombre, correo, foto))
        result = cursor
        conexion.commit()
        conexion.close()
        return result
    

# Update) ubicar por id el producto a modificar
def updEmpleadoById(idempleado, nombre, correo, foto):
    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE empleados SET nombre = %s, correo = %s, foto = %s WHERE idempleado = %s",(nombre, correo, foto, idempleado))
        result = cursor
    conexion.commit()
    conexion.close()
    return result

# Delete
def delEmpleadoById(id):
    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM empleados WHERE idempleado = %s", (id))
        result = cursor
    conexion.commit()
    conexion.close()
    return result