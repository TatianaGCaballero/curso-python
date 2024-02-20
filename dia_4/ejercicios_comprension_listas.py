'''
Para realizar el ejercicio a continuación, puedes optar por diferentes caminos.
Si bien en programación el camino correcto es el que devuelve el resultado correcto,
te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar
a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!
'''

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [valor**2 for valor in valores]
print(valores_cuadrado)

'''
Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. 
Si bien en programación el camino correcto es el que devuelve el resultado correcto, 
te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar 
a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!

Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.
'''
valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares = [valor % 2 == 0 for valor in valores]
print(valores_pares)

valores_pares = [valor for valor in valores if valor%2 == 0]
print(valores_pares)

'''
Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos 
mismos valores en una nueva lista de valores de temperatura en grados Celsius. 
La conversión entre tipo de unidades es la siguiente:

°C = (°F - 32) * (5/9)
'''
temperatura_fahrenheit = [32, 212, 275]

grados = [(temperatura - 32) * (5/9) for temperatura in temperatura_fahrenheit]
print(grados)