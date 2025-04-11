import tkinter as tk
from tkinter import messagebox
from mysql.connector import connect, Error

# Conexión a la base de datos
def conectar_bd():
    try:
        conexion = connect(
            host="localhost",
            user="usuario",
            password="contraseña",
            database="nombre_base_datos"
        )
        return conexion
    except Error as e:
        print(f"Error: {e}")
        return None

# Función para agregar una agencia espacial
def agregar_agencia():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    try:
        id = int(entry_id.get())
        nombre = entry_nombre.get()
        pais = entry_pais.get()
        fecha = entry_fecha.get()
        cursor.execute("INSERT INTO AgenciaEspacial (ID, Nombre, Pais, FechaCreacion) VALUES (%s, %s, %s, %s)", (id, nombre, pais, fecha))
        conexion.commit()
        messagebox.showinfo("Éxito", "Agencia agregada correctamente")
    except Error as e:
        messagebox.showerror("Error", f"Error al agregar agencia: {e}")
    finally:
        cursor.close()
        conexion.close()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Agencias Espaciales")

# Entradas para cada campo de agencia
tk.Label(root, text="ID:").grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)

tk.Label(root, text="Nombre:").grid(row=1, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=1, column=1)

tk.Label(root, text="País:").grid(row=2, column=0)
entry_pais = tk.Entry(root)
entry_pais.grid(row=2, column=1)

tk.Label(root, text="Fecha de Creación (AAAA-MM-DD):").grid(row=3, column=0)
entry_fecha = tk.Entry(root)
entry_fecha.grid(row=3, column=1)

# Botón para agregar agencia
btn_agregar = tk.Button(root, text="Agregar Agencia", command=agregar_agencia)
btn_agregar.grid(row=4, column=0, columnspan=2)

root.mainloop()
