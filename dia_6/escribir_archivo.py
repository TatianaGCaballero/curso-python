# w de escrinir y cambiar todo lo que haya

archivo = open('prueba1.txt','w')
resultado = archivo.write('holii soy tu nuevo archivo')
print(resultado)

archivo.close()

# saltos de linea con for

archivo = open('prueba2.txt', 'w')
lista = ['holi','tati']
for letra in lista:
    archivo.write(letra + '\n')
archivo.close()

# 'a' a;ade todo al final

archivo = open('texto.txt','a')
resultado = archivo.write('magister en recursos hidricos')
print(resultado)

archivo.close()