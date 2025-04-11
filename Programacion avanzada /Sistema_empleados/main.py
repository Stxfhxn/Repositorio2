# main.py
import registro
import antiguedad
import beneficios

def main():
    empleados = {}
    nombre = "Juan Martínez"
    salario = 70000
    fecha_ingreso = "01/08/2018"

    # Registrar empleado
    empleados = registro.agregar_empleado(empleados, nombre, salario, fecha_ingreso)

    # Calcular antigüedad
    antig = antiguedad.calcular_antiguedad(empleados[nombre]["fecha_ingreso"])
    
    # Asignar beneficios
    beneficios_asignados = beneficios.asignar_beneficios(antig)

    # Mostrar información
    print("\n--- Información del Empleado ---")
    print(f"Nombre: {nombre}")
    print(f"Salario: ${salario}")
    print(f"Fecha de Ingreso: {fecha_ingreso}")
    print(f"Antigüedad: {antig} años")
    print(f"Beneficios asignados: {', '.join(beneficios_asignados) if beneficios_asignados else 'Sin beneficios adicionales'}")

if __name__ == "__main__":
    main()
