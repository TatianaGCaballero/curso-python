from random import *


def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2

def evaluar_jugada(dado1, dado2):
    suma = dado1 + dado2
    if suma <= 6:
        return f'La suma de tus dados es {suma}. Lamentable'
    elif suma > 6 and suma < 10:
        return f'La suma de tus dados es {suma}. Tienes buenas chances'
    else:
        return f'La suma de tus dados es {suma}. Parece una jugada ganadora'



resultado1, resultado2 = lanzar_dados()

resultado = evaluar_jugada(resultado1, resultado2)
print(resultado)


lista = [1,2,2,3,1,4,5,4]

def reducir(lista):
    lista2 = list(set(lista))
    lista2.pop(-1)
    return lista2

def promedio(lista2):
    valor = sum(lista2)/len(lista2)
    return valor

lista_limpia = reducir(lista)
resultado1 = promedio(lista_limpia)
print(resultado1)



lista_numeros = [1,2,3,4,5,6]
def lanzar_moneda():
    lista = ['cara', 'cruz']
    azar_2 = choice(lista)
    return azar_2

def probar_suerte(azar_2,lista_numeros):
    if azar_2 == 'cara':
        print('la lista se destruye')
        lista_vacia = lista_numeros.remove()
        return lista_vacia

    else:
        print('salvado')
        return lista_numeros

azar_2 = lanzar_moneda()
resultado_3 = probar_suerte(azar_2,lista_numeros)
print(resultado_3)



