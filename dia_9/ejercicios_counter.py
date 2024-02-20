from collections import Counter
# cuenta cuanta veces esta undijito o una palabra
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)
print(contador)


# palabras
palabra = 'missisiipi'
contador = Counter(palabra)
print(contador)

# frases

frase = 'al pan pan y al vino vino'
contador = Counter(frase.split())
print(contador)

# mas comun most_common

serie = Counter([1,1,1,2,2,2,3,3,3,3])
print(serie.most_common())

# que numeros muestro con mas repetidos

serie = Counter([1,1,1,2,2,2,3,3,3,3])
print(serie.most_common(2))




