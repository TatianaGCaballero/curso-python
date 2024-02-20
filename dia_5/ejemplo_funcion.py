from random import *

precios_cafe = [('capucchino', 1.5), ('expresso', 2.4)]


def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro, precio_mayor)


cafe, precio = cafe_mas_caro(precios_cafe)
print(cafe, precio)


def lanzar_dados() -> object:
    return randint(1, 6), randint(1, 6)


resultado = lanzar_dados()
print(resultado)
