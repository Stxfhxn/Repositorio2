import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(
            host='localhost',          # Nombre del host
            database='nombre_base_datos',  # Nombre de la base de datos
            user='usuario',               # Usuario de la base de datos
            password='contraseña'         # Contraseña del usuario
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
        return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
