import time
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)

    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador = contador + 1

    return lista

# print(prueba_for(100))
# print(prueba_while(100))

inicio = time.time()
prueba_for(15)
final = time.time()
print(final - inicio)

inicio = time.time()
prueba_while(15)
final = time.time()
print(final - inicio)
