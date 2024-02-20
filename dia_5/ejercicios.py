""" Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.
"""


def devolver_distintos(a, b, c):
    total = a + b + c
    lista = [a, b, c]
    if total > 15:
        return max(lista)
    elif total < 10:
        return min(lista)
    else:
        return lista


resultado = devolver_distintos(2, 3, 12)
print(resultado)

""" Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d'
,
'e'
,
'i'
,
'n'
,
'o'
,
'r'
,
't'] """


def sin_repetir(palabra):
    mi_set = set()

    for letra in palabra:
        mi_set.add(letra)

    mi_lista = list(mi_set)
    mi_lista.sort()
    return mi_lista


resultado = sin_repetir('tatiana')
print(resultado)

""" Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas """


def argumentos(*args):
    lista = []
    for arg in args:
        lista.append(arg)
        if arg == 0:
            return True
        else:
            return False




resultado = argumentos(1,2,3,5,5)
print(resultado)

""" Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos """


def contar_primos(num1):
    for n in range(2,num1):
        if num1 % n == 0:
            print('no es primo')
        else:
            print('es primo')


resultado = contar_primos(23)

