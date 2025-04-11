import mysql.connector

# Configuración de la conexión
def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",          # Dirección del servidor
            user="tu_usuario",         # Usuario de MySQL
            password="tu_contraseña",  # Contraseña de MySQL
            database="AgenciasEspaciales"  # Nombre de la base de datos
        )
        print("Conexión exitosa a la base de datos")
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None
