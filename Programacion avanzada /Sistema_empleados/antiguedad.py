# antiguedad.py
from datetime import datetime

def calcular_antiguedad(fecha_ingreso):
    fecha_ingreso_dt = datetime.strptime(fecha_ingreso, "%d/%m/%Y")
    fecha_actual = datetime.now()
    antiguedad = fecha_actual.year - fecha_ingreso_dt.year
    if fecha_actual.month < fecha_ingreso_dt.month or (fecha_actual.month == fecha_ingreso_dt.month and fecha_actual.day < fecha_ingreso_dt.day):
        antiguedad -= 1
    return antiguedad
