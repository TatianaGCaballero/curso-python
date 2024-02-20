# para abrir y mostrar en pantalla open() y read()
mi_archivo = open('texto.txt')
leer = mi_archivo.read()
print(leer)

# para mostrar la primera linea
mi_archivo = open('texto.txt')
leer = mi_archivo.readline()
print(leer)

# para kostrar otra linea
mi_archivo = open('texto.txt')
leer = mi_archivo.readline()

leer = mi_archivo.readline()
print(leer)

# se pueden usar metodos de string
mi_archivo = open('texto.txt')
for l in mi_archivo:
    print(' aqui dice ' + l)


# para listas readlines() muesta todo
mi_archivo = open('texto.txt')
todas = mi_archivo.readlines()
todas = todas.pop()
print(todas)


mi_archivo.close()
