palabra = 'tati'
lista =[]

for letra in palabra:
    lista.append(letra)
print(lista)

lista = [letra for letra in 'tati']
print(lista)

# por rangos
lista = [n for n in range(1,10,34)]
print(lista)

# division por 2

lista = [n/2 for n in range(0,21,2)]
print(lista)

lista = [n for n in range(0,21,2) if n*2>10]
print(lista)