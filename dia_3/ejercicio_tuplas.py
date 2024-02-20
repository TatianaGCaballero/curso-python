'''
Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla,
y muestra el resultado (integer) en pantalla:
'''


mi_tupla = (1,2,3,2,2,3,4,5,6,5,5,5,4,3,3,3)
resultado = mi_tupla.count(2)
print(resultado)

# Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista

mi_tupla = (1,2,3,2,2,3,4,5,6,5,5,5,4,3,3,3)
lista = list(mi_tupla)
print(lista)

# Extrae los elementos de la siguiente tupla en cuatro variables:
mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla
print(a,b,c,d)
