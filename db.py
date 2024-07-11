# instalar pymysql -> pip install pymysql
# importar pymysql / SQLachemy / dbmysql
import pymysql

# conectar con el servidor MySQL
def conectarMySQL():
    # datos sensibles -> variables de entorno
    
    # local
    host="localhost"
    user="root"
    password="root"
    db="empleados_db"
    
    # deploy -> Pythonanywhere
    # host="guidovarela.mysql.pythonanywhere-services.com"
    # user="guidovarela"
    # clave="codo2024"
    # db="guidovarela$tienda-py"

    return pymysql.connect(host=host,user=user,password=password,database=db)