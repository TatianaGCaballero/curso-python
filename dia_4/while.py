monedas = 5

while monedas > 0:
    print('tengo {monedas} monedas')
    monedas = monedas - 1
else:
    print('no tengo mas dinero')

respuesta = 's'

while respuesta == 's':
    respuesta = input('quieres seguir s/n ')
else:
    print('gracias')


respuesta = 's'
while respuesta == 's':
    respuesta = input('quieres seguir s/n ')
    pass
print('hola')

# si quiero interrumpir break
nombre = input('dime tu nombre: ')

for letra in nombre:
    if letra == 't':
        break
    print(letra)

# continue: para y se vuelve al inicio

nombre = input('dime tu nombre: ')
for letra in nombre:
    if letra == 'i':
        continue
    print(letra)











