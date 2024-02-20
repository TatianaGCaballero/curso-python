import os
from Pathlib import Path

# mostrar ruta

ruta = os.getcwd()
print(ruta)

# cambiar de directorio
os.chdir('C:/Users/yeisoncaicedo/Desktop/python/pythonProject')
archivo = open('otro_archivo.txt')
print(archivo.read())

# crear carpeta
os.makedirs('C:/Users/yeisoncaicedo/Desktop/python/pythonProject/dia_7')

# buscar la basename
# ruta = 'C:\\Users\\Tatica\\Desktop\\python\\pythonProject\\dia_6//texto.txt'

elemento = os.path.basename(ruta)
print(elemento)

# nombre de l dorectorio

ruta = 'C:\\Users\\Tatica\\Desktop\\python\\pythonProject\\dia_6//texto.txt'
elemento = os.path.dirname(ruta)
print(elemento)

# dividir directorio del elemento
ruta = 'C:\\Users\\Tatica\\Desktop\\python\\pythonProject\\dia_6//texto.txt'
elemento = os.path.split(elemento)
print(elemento)

# que se pueda leer en cualquier sisitema operativo
carpeta = Path('C:/Users/Tatica/Desktop/python/pythonProject/dia_6/texto.txt')
archivo = carpeta / 'texto.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())


