# Definición de la lista para almacenar los sabores de helado
inventario_helados = []

# Función para registrar un sabor de helado
def registrar_sabor(nombre, precio, stock):
    helado = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    inventario_helados.append(helado)

# Función para mostrar la información de los sabores de helado registrados
def mostrar_inventario():
    print("Información registrada de sabores de helado:")
    for helado in inventario_helados:
        print(f"{helado['nombre']} Precio: {helado['precio']}, Stock: {helado['stock']}")

# Datos de prueba
registrar_sabor("Chocolate", 2.5, 100)
registrar_sabor("Vainilla", 2.0, 80)
registrar_sabor("Fresa", 3.0, 70)

# Mostrar inventario de helados
mostrar_inventario()
