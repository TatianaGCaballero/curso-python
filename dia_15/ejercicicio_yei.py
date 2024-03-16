from collections import Counter

# la letra que mas se repita en una palabra

# 1 forma
palabra = 'tatiana'
resultado = Counter(palabra)
print(resultado)

forma_2 = Counter('tatiana caballero')
resultado = forma_2.most_common(1)
print(resultado)

palabra = 'tatiana'

resultado = palabra.count('a')
print(resultado)



def letra_mas_repite(palabra_2):
    mi_dict = {}
    letra_mas_repetida = ''
    veces_que_aparece = 0
    for letra in palabra_2:
        if letra in mi_dict:
            mi_dict[letra] = mi_dict[letra] + 1
        else:
            mi_dict[letra] = 1

    for letra, ocurrencia in mi_dict.items():
        if ocurrencia > veces_que_aparece:
            veces_que_aparece = ocurrencia
            letra_mas_repetida = letra

    return letra_mas_repetida


resultado = letra_mas_repite('tatiana es la mejor esposa')
print(resultado)


