import timeit

declaracion = '''
      prueba_for(10)

'''

mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)

    return lista

'''

duracion = timeit.timeit(declaracion, mi_setup, number = 1000)
print(duracion)
