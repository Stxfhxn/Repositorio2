# beneficios.py
def asignar_beneficios(antiguedad):
    beneficios = []
    if antiguedad > 3:
        beneficios.append("Bono anual")
    if antiguedad > 5:
        beneficios.append("Días adicionales de vacaciones")
    return beneficios
