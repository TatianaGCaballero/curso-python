'''
Desafío: Suma de Dos Números

# Escribe una función llamada 'suma_dos_numeros' que tome una
lista de números y un objetivo.
# La función debe devolver los índices de los dos números en
la lista que suman al objetivo.

# Puedes asumir que siempre hay una única solución y no puedes
usar el mismo elemento dos veces.

# Ejemplo:
# suma_dos_numeros([2, 7, 11, 15], 9) debería devolver [0, 1] ya
que nums[0] + nums[1] = 2 + 7 = 9.
'''


lista = [2, 7, 11, 7]
def suma_dos_numeros(lista, obj):
    primer_numero = lista[0]
    lista.pop(0)
    for i, numero in enumerate(lista):
        if primer_numero + numero == obj:
            return [0, i+1]

    for j in (i + 1, lista):
        if lista[i] + lista[j] == obj:
            return [i,j]





resultado = suma_dos_numeros(lista, 9)
print(resultado)


def suma_dos_numeros(nums, objetivo):
    # Diccionario para almacenar el complemento de cada número
    complementos = {}

    for i, num in enumerate(nums):
        complemento = objetivo - num

        # Verificar si el complemento ya está en el diccionario
        if complemento in complementos:
            return [complementos[complemento], i]

        # Si no está, almacenar el número actual y su índice
        complementos[num] = i


# Prueba la función con diferentes casos
resultado = suma_dos_numeros([1, 7, 5, 4], 9)
print(resultado)














