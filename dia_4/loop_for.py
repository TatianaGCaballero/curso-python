lista = ['a', 'b', 'c']

for letra in lista:
    print('letra: ' + letra)

lista = ['a', 'b', 'c']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f'letra {numero_letra}: {letra}')

lista = ['lina', 'gema', 'tati']

for nombre in lista:
    if nombre.startswith('k'):
        print(nombre)
    else:
        print('no coincide la letra')

numeros = [1, 2, 3, 4, 5]
mi_valor: int = 0

for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)

palabra = 'python'

for letra in palabra:
    print(letra)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

dic = {'clave1':'a', 'clave2': 'b'}
for item in dic.items():
    print(item)

dic = {'clave1':'a', 'clave2': 'b'}
for item in dic.values():
    print(item)

dic = {'clave1':'a', 'clave2': 'b'}

for a,b in dic.items():
    print(a,b)





