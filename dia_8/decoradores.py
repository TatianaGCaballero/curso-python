def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())


mi_funcion = mayuscula
mi_funcion('tati')

# funcion como argumento de otra funcion

def una_funcion(funcion):
    return funcion

una_funcion(mayuscula('probando'))

def cambiar_letra(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())
    if tipo == 'may':
        return mayuscula
    elif tipo == 'min':
        return minuscula

    operacion = cambiar_letra('may')
    operacion('palabra')
# decorar


def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')

    return otra_funcion


@decorar_saludo
def mayuscula(texto):
        print(texto.upper())

@decorar_saludo
def minuscula(texto):
        print(texto.lower())

minuscula('PYTHON')


# 2 forma de decorar
mayuscula_decorada = decorar_saludo(mayuscula)
mayuscula_decorada('yeisiton')




