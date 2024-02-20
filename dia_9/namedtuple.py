from collections import namedtuple

# tupla dominada

Persona = namedtuple('persona', ['nombre','peso'])
tati = Persona('tatiana', 54)
print(tati.nombre)
print(tati[1])