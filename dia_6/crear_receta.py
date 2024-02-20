import os
from pathlib import Path

nombre = input('dime tu nombre: ')
print(f'hola {nombre} bienvenido/a')

guia = Path(Path.home(), 'Recetas')
for txt in Path(guia).glob('**/*.txt'):
    print(txt)


def pedir_receta():
    intento = ''
    while intento not in ['1','2','3','4','5']:
        intento = input('elige un numero del 1 al 5: ')

        if intento == '1':
            pregunta = input('c/e/p/po:')
            if pregunta == 'c':
                pregunta_2 = input('que receta quieres e/m: ')
                if pregunta_2 == 'e':

                    ruta = os.chdir('C:\\Users\\Tatica\\Recetas\\Carnes')

                    archivo = open('Entrecot al Malbec.txt','r')
                    print(archivo.read())
                    archivo.close()
                if pregunta_2 == 'm':
                    mi_archivo = open(' Matambre a la Pizza.txt')
                    mi_archivo.read()
                    mi_archivo.close()
            if pregunta == 'e':
                pregunta_2 = input('que receta quieres eg/me: ')
                if pregunta_2 == 'eg':
                    mi_archivo = open(' Ensalada Griega.txt')
                    mi_archivo.read()
                    mi_archivo.close()
            if pregunta == 'p':
                pregunta_2 = input('que receta quieres c/r: ')
                if pregunta_2 == 'c':
                    mi_archivo = open('Canelones de Espinaca.txt')
                    mi_archivo.read()
                    mi_archivo.close()
                if pregunta_2 == 'r':
                    mi_archivo = open('Ravioles de Ricotta.txt')
                    mi_archivo.read()
                    mi_archivo.close()
            if pregunta == 'po':
                pregunta_2 = input('que receta quieres c/t: ')
                if pregunta_2 == 'c':
                    mi_archivo = open('Compota de Manzana.txt')
                    mi_archivo.read()
                    mi_archivo.close()
                if pregunta_2 == 't':
                    mi_archivo = open('Tarta de Frambuesa.txt')
                    mi_archivo.read()
                    mi_archivo.close()
        if  intento == '2':
            pregunta = input('c/e/p/po:')
            if(pregunta == 'c' or pregunta == 'e' or pregunta == 'p' or pregunta == 'po'):
                ruta = os.chdir('C:\\Users\\Tatica\\Recetas')

                archivo = open('pollo.txt', 'w')
                archivo.write('recetaa')
                archivo.close()
        if intento == '3':
            pregunta = input('di una categoria: ')
            archivo = open(pregunta, 'r')
            archivo.read()









    return int(intento)

intento_1 = pedir_receta()
print(intento_1)


