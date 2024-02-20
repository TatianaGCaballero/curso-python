nombre = input('cual es tu nombre: ')

ventas = input('cuanto vendiste: ')

conversion_ventas = float(ventas)

porciento = 13 * conversion_ventas

division = porciento/100

redondeo = round(division, 1)

print(f'Hola {nombre}, tu comision este mes es {redondeo}')


