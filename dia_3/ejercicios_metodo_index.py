# Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"

palabra = 'ordenador'
resultado = palabra[4]
print(resultado)

# Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:

frase = 'En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son.'
resultado = frase.index('práctica')
print(resultado)

# Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase

frase = 'En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son.'
resultado = frase.rindex('práctica')
print(resultado)