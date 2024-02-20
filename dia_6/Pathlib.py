from pathlib import Path

carpeta = Path('C:/Users/Tatica/Desktop/python/pythonProject/dia_6/texto.txt')
print(carpeta.read_text())

# nombre aarchivo
carpeta = Path('C:/Users/Tatica/Desktop/python/pythonProject/dia_6/texto.txt')
print(carpeta.name)

# termonacion
carpeta = Path('C:/Users/Tatica/Desktop/python/pythonProject/dia_6/texto.txt')
print(carpeta.suffix)

# nombre sin e txt
carpeta = Path('C:/Users/Tatica/Desktop/python/pythonProject/dia_6/texto.txt')
print(carpeta.stem)

# verificar si metodo existe

if not carpeta.exists():
    print('no existe')
else:
    print('existe')







