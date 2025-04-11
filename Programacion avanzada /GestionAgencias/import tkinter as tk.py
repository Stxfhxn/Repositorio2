import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

# Conexión a la base de datos
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="ExploracionEspacial"
    )

# Función para mostrar las agencias espaciales
def mostrar_agencias():
    for item in tree.get_children():
        tree.delete(item)
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM AgenciaEspacial")
    for fila in cursor.fetchall():
        tree.insert("", tk.END, values=fila)
    conexion.close()

# Función para agregar una agencia
def agregar_agencia():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        id = int(entry_id.get())
        nombre = entry_nombre.get()
        pais = entry_pais.get()
        fecha = entry_fecha.get()
        consulta = "INSERT INTO AgenciaEspacial (ID, Nombre, Pais, FechaCreacion) VALUES (%s, %s, %s, %s)"
        cursor.execute(consulta, (id, nombre, pais, fecha))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Éxito", "Agencia agregada exitosamente.")
        mostrar_agencias()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Función para eliminar una agencia
def eliminar_agencia():
    try:
        seleccion = tree.selection()
        if not seleccion:
            raise Exception("Selecciona una agencia para eliminar.")
        id = tree.item(seleccion, "values")[0]
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM AgenciaEspacial WHERE ID = %s", (id,))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Éxito", "Agencia eliminada exitosamente.")
        mostrar_agencias()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Gestión de Agencias Espaciales")
ventana.geometry("600x400")

frame_form = tk.Frame(ventana)
frame_form.pack(pady=10)

tk.Label(frame_form, text="ID:").grid(row=0, column=0, padx=5, pady=5)
entry_id = tk.Entry(frame_form)
entry_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(frame_form)
entry_nombre.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_form, text="País:").grid(row=2, column=0, padx=5, pady=5)
entry_pais = tk.Entry(frame_form)
entry_pais.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Fecha (YYYY-MM-DD):").grid(row=3, column=0, padx=5, pady=5)
entry_fecha = tk.Entry(frame_form)
entry_fecha.grid(row=3, column=1, padx=5, pady=5)

tk.Button(frame_form, text="Agregar Agencia", command=agregar_agencia).grid(row=4, column=0, columnspan=2, pady=10)

tree = ttk.Treeview(ventana, columns=("ID", "Nombre", "Pais", "Fecha"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Pais", text="País")
tree.heading("Fecha", text="Fecha")
tree.pack(pady=10, fill="x")

tk.Button(ventana, text="Eliminar Agencia", command=eliminar_agencia).pack(pady=5)

mostrar_agencias()

ventana.mainloop()
