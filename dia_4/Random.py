from random import *

# randint
aleatorio = randint(1,50)
print(aleatorio)

# uniform
aleatorio = uniform(1,5)
print(aleatorio)

aleatorio = round(uniform(1,5))
print(aleatorio)

# random
aleatorio = random()
print(aleatorio)

# choice
lista = ['azul', 'amarillo', 'verde']
aleatorio = choice(lista)
print(aleatorio)

# shuffle
num = list(range(1,10))
shuffle(num)
print(num)


