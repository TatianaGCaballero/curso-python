'''
Utilizando las variables num1 y num2, que se alimentan con el input del usuario (tal como en el código ya proporcionado):

Crea una estructura de control de flujo que compare los valores de las variables, y arroje un resultado de acuerdo al caso:

"num1 es mayor que num2"

"num2 es mayor que num1"

"num1 y num2 son iguales"

Debes mostrar en pantalla el valor de las variables ingresadas en lugar de num1 y num2
'''

num1 = int(input('Ingresa un numero: '))
num2 = int(input('Ingresa un numero: '))

if num1 > num2:
    print(f'{num1} es mayor que {num2}')

elif num2 > num1:
    print(f'{num2} es mayor que {num1}')

else:
    print(f'{num1} y {num2} son iguales')

'''
Las leyes de un país establecen que un adulto puede conducir si tiene licencia para hacerlo, 
y para optar por una licencia para conducir, debe de tener 18 años o más.

Crea una estructura condicional para verificar si una persona de 16 años sin licencia puede conducir, 
y muestra el resultado que corresponda en pantalla:

"Puedes conducir"

"No puedes conducir aún. Debes tener 18 años y contar con una licencia"

"No puedes conducir. Necesitas contar con una licencia"
'''

edad = 16
licencia = False

if edad >= 18 and licencia:
    print('puedes conducir')
elif edad < 18:
    print('no puedes conducir aun')
else:
    print('no tienes licencia')

'''
Para acceder a un determinado puesto de trabajo, el candidato debe ser capaz de programar en Python y tener conocimientos de inglés.

Crea una estructura condicional para evaluar a un candidato dadas estas condiciones, y muestra el mensaje correspondiente en pantalla:

"Cumples con los requisitos para postularte"

"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"

"Para postularte, necesitas tener conocimientos de inglés"

"Para postularte, necesitas saber programar en Python"

'''

habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python:
    print('cumples con los requisitos')
elif not habla_ingles:
    print('no tienes conocimientos de ingles')
else:
    print('debes saberprogramar')