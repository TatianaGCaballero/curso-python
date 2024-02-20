'''
Imprime en pantalla frases como la siguiente:
'{nombre} se encuentra en el índice {indice}'
Donde nombre debe ser cada uno de los nombres de la lista a continuación,
y el índice, obtenido mediante enumerate().
'''

lista_nombres = ['tati', 'yei', 'marcos', 'rosa', 'lala', 'nata']
indice = 0

for nombre in lista_nombres:
    print(f'{nombre} esta en el indice {indice}')
    indice = indice + 1

'''
Crea una lista formada por las tuplas (indice, elemento), 
formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".
Llama a la lista obtenida con el nombre de variable lista_indices .
'''

lista_indices = list(enumerate('python'))
print(lista_indices)

'''
Imprime en pantalla únicamente los índices de aquellos nombres de la lista 
a continuación, que empiecen con M:'''

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for items, nombre in enumerate(lista_nombres):
    if nombre[0] == 'M':
        print(items)
