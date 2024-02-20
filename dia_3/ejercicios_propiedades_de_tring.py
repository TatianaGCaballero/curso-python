'''
Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla.
Por suerte, conoces que los strings son multiplicables y puedes realizar esta actividad de forma simple y elegante
'''

texto = 'Repeticion'
resultado = texto * 15
print(resultado)

'''
Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.

Tierra mojada,

mis recuerdos de viaje

entre las lluvias
'''

poema = '''Tierra mojada,

mis recuerdos de viaje

entre las lluvias
'''

resultado = 'agua' not in poema
print(resultado)


# Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista.

palabra = 'electroencefalografista'
largo = len(palabra)
print(largo)
