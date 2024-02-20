import re
texto = 'si necesita ayuda lla,a al (565)-566-544'
patron = 'ayuda'

busqueda = re.search(patron,texto)
print(busqueda)
# ubicacion de la palabra
print(busqueda.span())
print(busqueda.start())

texto = 'llama al 564-543-567'
patron = r'\d\d\d-\d\d\d-\d\d\d'

resultado = re.search(patron,texto)
print(resultado)
# para mostrar el numero
print(resultado.group())

# clave

clave = input('escribe una clave: ')
patron = r'\D{1}\w{7}'

chequear = re.search(patron,clave)
print(chequear)

