from random import shuffle

# elige el palito
# lista inicial
palitos = ['-', '--', '---', '----']


# mezcalr palitos

def mezclar(lista):
    shuffle(lista)
    return lista


# pedir u intento
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input('elige un numero del 1 al 4: ')
    return int(intento)


# comprobar untento

def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print('lo siento')
    else:
        print('te salvaste')


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()

resultado = chequear_intento(palitos_mezclados,seleccion)
print(resultado)
