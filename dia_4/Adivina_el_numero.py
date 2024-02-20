from Random import *

intentos = 0

numero_secreto = randint(1, 100)

nombre = input('Dime tu nombre: ')


print(f'Bueno {nombre} he pensado un # entre 1 y 100\nTienes 8 intentos')


while intentos < 8:
    estimado = int(input('dime un numero: '))
    intentos = intentos + 1

    if estimado < numero_secreto:
        print('numero incorrecto')

    elif estimado > numero_secreto:
        print('incorrecto')

    elif estimado < numero_secreto:
        print('incorrecto')

    else:
        print('adivinaste')
        break

if estimado != numero_secreto:
    print("sigue intentando")
