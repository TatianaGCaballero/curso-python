lista = [1,1,2,2,3,3,4,5,6,6]

def numero_repetido(lista):
    lista_vacia = []

    for numero in lista:
        if numero not in lista_vacia:
            lista_vacia.append(numero)
        else:
            lista_vacia.remove(numero)

    return lista_vacia

resultado = numero_repetido(lista)
print(resultado)
