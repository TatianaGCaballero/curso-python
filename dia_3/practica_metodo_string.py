# Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:

frase = 'Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar.'

resultado = frase.upper()

print(resultado)

'''
Une la siguiente lista en un string, separando cada elemento con un espacio. 
Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
'''

lista_palabras = ['la', 'legibilidad', 'cuenta']
resultado = ' '.join(lista_palabras)
print(resultado)

'''
Reemplaza en la siguiente frase:

"Si la implementación es difícil de explicar, puede que sea una mala idea."

los siguientes pares de palabras:

"difícil" --> "fácil"

"mala" --> "buena"

y muestra en pantalla la frase con ambas palabras modificadas.
'''

frase = 'Si la implementación es difícil de explicar, puede que sea una mala idea.'

resultado = frase.replace('difícil', 'facil')
print(resultado)

resultado2 = frase.replace('mala', 'buena')

print(resultado2)

# si la quiero los cambios en la misma frase

resultado_final = frase.replace('difícil','facil').replace('mala', 'buena')

print(resultado_final)