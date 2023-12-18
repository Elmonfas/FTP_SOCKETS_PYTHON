import pymysql
conexion = pymysql.connect(host='localhost', user='root', password='elmonfas', database='ejer6_DWES')

def agregar_usuario(nombre, email, contrasena, mensaje):
    cursor = conexion.cursor()
    query = "INSERT INTO USUARIOS(user_name, user_email, user_pass, user_msg) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nombre, email, contrasena, mensaje))
    conexion.commit()
