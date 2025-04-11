with open('file.json', 'r') as file:
    file.seek(0)  # Va al inicio
    content = file.read(100)  # Lee solo los primeros 100 bytes
    print(content)
