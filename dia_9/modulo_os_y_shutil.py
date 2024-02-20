# para saber en que directorio estoy
import os
# para ver la base
from pathlib import Path

# importar shutil
import shutil

import send2trash

print(os.getcwd())

# crear un texto

archivo = open('curso.txt', 'w')
archivo.write('holii soy la biologa tatiana')
archivo.close()

# para mostrar en python lo que tengo en determinda direccion en la que estoy

print(os.listdir())

# para mover archivos ya tenemos el metodo shutil
# shutil.move('curso.txt', 'C:/Users/caica/Desktop/python/pythonProject/dia_1')

# para ver la base de mi pc
base = Path.home()
print(base)

# eliminar archivos
send2trash.send2trash('curso.txt')

# metodo walk

# recorre todo un directorio

print(os.walk('C:/Users/caica/Desktop/ejemplo/ejemplo2'))

for carpeta, subcarpeta,archivo in os.walk('C:/Users/caica/Desktop/ejemplo/ejemplo2'):
    print(f'en la carpeta: {carpeta}')

