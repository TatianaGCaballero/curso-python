'''
Crea una función (todos_positivos) que reciba una lista de números como parámetro,
y devuelva True si todos los valores de una lista son positivos, y False si al menos
uno de los valores es negativo. Crea una lista llamada lista_numeros
con valores positivos y negativos.
'''

lista = [1,2,3,-4,-6,7,-9]


def positivos(lista):
    for numeros in lista:
        if numeros < 0:
            return False
        else:
            pass

    return True


resultado = positivos(lista)
print(resultado)

'''
Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) 
siempre y cuando sean mayores a 0 y menores a 1000, 
y devuelva el resultado de dicha suma.
'''

lista = [4,6,7,499,233,4556,32]



def suma(lista):
    suma1 = 0
    for numero in lista:
        if numero > 0 and numero < 1000:
            suma1 = suma1 + numero

    return suma1


resultado = suma(lista)
print(resultado)


lista_numeros = [4,6,7,499,233,4556,32]


def suma_menores(lista_numeros):
    suma = 0

    for numero in lista_numeros:
        if numero in range(0, 1000):
            suma = suma + numero

        else:
            pass
    return suma

resultado = suma_menores(lista_numeros)
print(resultado)


'''Crea una función (cantidad_pares) que cuente la cantidad de números pares que 
existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.
'''

lista = [2,1,3,4,5,6,7,8,9,10,54]

def pares(lista):
    cantidad = 0
    for par in lista:
        if par%2 == 0:
            cantidad = cantidad + 1
        else:
            pass
    return cantidad

resultado = pares(lista)
print(resultado)
