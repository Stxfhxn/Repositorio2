import json
import os

# Función para cargar datos desde un archivo JSON
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return []

# Función para guardar datos en un archivo JSON
def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
