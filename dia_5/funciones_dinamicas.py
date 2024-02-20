def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100, 1000):
            return True
        else:
            pass

    return False


resultado = chequear_3_cifras([12, 34, 567])
print(resultado)


def lista_3_cifras(lista):
    lista_2 = []
    for n in lista:
        if n in range(100, 1000):
            lista_2.append(n)
        else:
            pass
    return lista_2


resultado = lista_3_cifras([453, 54, 567])
print(resultado)
