from collections import defaultdict

# para añadir algo que no exista y que no salga error

mi_diccionario = defaultdict(lambda: 'holiii')
mi_diccionario['edad'] = 25
print(mi_diccionario)

