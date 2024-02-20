from random import *

'''
Implementa la función randint() de la librería random que te permita obtener 
un número entero del 1 al 10, y almacena dicho valor en una variable llamada aleatorio
'''
aleatorio = randint(1,10)
print(aleatorio)

'''
Implementa la función random() de la librería random que te permita obtener un número 
decimal entre 0 y 1, y almacena dicho valor en una variable llamada aleatorio
'''

aleatorio = random()
print(aleatorio)

'''
Utiliza el método choice() de la librería random para obtener un elemento 

al azar de la lista de nombres a continuación, y almacena el nombre escogido en una variable llamada sorteo.
'''

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

aleatorio = choice(nombres)
print(aleatorio)