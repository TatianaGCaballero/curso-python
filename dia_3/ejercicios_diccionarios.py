# Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona

mi_dict = {
    'nombre': 'tatiana',
    'apellido': 'gomez',
    'edad': 25,
    'ocupacion': 'biologa'
}

print(mi_dict)

'''
Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.
Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se encuentre en esa misma posición. 
Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda.
'''
mi_dict = {"valores_1":{"v1":3,"v2":6},
           "puntos":{"points1":9,"points2":[10,300,15]}
           }

resultado = mi_dict['puntos']['points2'][1]
print(resultado)

'''
Actualiza la información de nuestro diccionario llamado mi_dic  
(reasignando nuevos valores a las claves según corresponda), 
y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:
'''

mi_dict = {
    'nombre': 'tatiana',
    'apellido': 'gomez',
    'edad': 25,
    'ocupacion': 'biologa'
}

mi_dict['edad'] = 26
mi_dict['ocupacion']= 'magister'

print(mi_dict)