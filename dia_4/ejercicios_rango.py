# Crea una lista formada por todos los números desde el 2500 al 2585 (inclusive). Almacena dicha lista en la variable

mi_lista = list(range(2501,2585))
print(mi_lista)

'''
Utilizando la función range(), crea en una única linea de código una lista formada 
por todos los números múltiplos de 3 desde el 3 al 300 (inclusive). Almacena dicha lista en la variable mi_lista
'''

mi_lista = list(range(3,300,3))
print(mi_lista)

'''
Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). 
Almacena el resultado en una variable llamada suma_cuadrados
'''
suma_cuadrados = 0
for i in range(1,15):
    suma_cuadrados = suma_cuadrados + i**2

print(suma_cuadrados)
