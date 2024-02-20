# letras que eligio

texto = input('escribe un texto: ')

print(texto)

letras = input('escribe 3 letras: ')
print(letras)
letras_2 = letras.lower()
# pasar las letras a una lista

lista = list(letras_2)
print(lista)

# poner minusculas texto y letras

minus = texto.lower()
print(minus)


# mirar cuantas veces aparecen lasletras en el texto

resultado_2 = minus.find('t')
print(resultado_2)

# largo de la lista

largo = len(minus)
print(largo)

# primero y ultimo elemento

indexacion = minus[0]
print(indexacion)

indexacion_2 = minus[-1]
print(indexacion_2)

# revertir el orden las palabraa

lista_2 = list(minus)
print(lista_2)

lista_2.reverse()

print(lista_2)


# encontrar si una palabra esta en el texto

boleano = 'python' in minus
print(boleano)

# diccionario

mi_dic = {'esta': True, 'no esta': False}
print(mi_dic)

