# enumerar

lista = ['a','b']
indice = 0

for item in lista:
    indice = indice +1
    print(indice,item)

lista = ['a','b']
for item in enumerate(lista):
    print(item)

lista = ['a','b']
for indice,item in enumerate(lista):
    print(indice,item)

# pasar a listade  tuples

lista = ['a','b','c']
lista_2 = list(enumerate(lista))
print(lista_2)



