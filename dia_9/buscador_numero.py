import os
import time
import datetime
import re
from pathlib import Path
import math
# ruta en donde esta la carpetA
ruta = '/Users/caica/Desktop/mi_directory'
print(ruta)

# contabilizar el tiempo
inicio = time.time()

# fecha de ejecucion del codigo
fecha = datetime.date.today()
print(fecha)

# patron que busco
patron = r'N\D{3}\d{5}'

numeros_encontrados = []

archivos_encontrados = []


# metodo walk

'''for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'las carpetas son {carpeta}')
    print('las subcarpetas son: ')
    for sub in subcarpeta:
        print(f'las subcarpetas son {sub}')
    for arch in archivo:
        print(f'los archivos son {arch}')

    print('\n')'''

# buscar el numero del patron
def buscar_numero(archivo, mi_patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(mi_patron, texto):
        return re.search(mi_patron, texto)
    else:
        return ''




# mostrar cuales tienen los patrones


def crear():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for arch in archivo:
            resultado = buscar_numero(Path(carpeta,arch), patron)
            if resultado != '':
                numeros_encontrados.append((resultado.group()))



def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de Búsqueda: {fecha.day}/{fecha.month}/{fecha.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')
    for a in archivos_encontrados:
        print(f'{a}\t{numeros_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Números encotrados: {len(numeros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)

crear()
mostrar_todo()