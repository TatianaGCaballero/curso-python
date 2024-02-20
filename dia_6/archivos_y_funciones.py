'''Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro,
y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"
'''


def sobrescribir(argumento):
    mi_archivo = open(argumento, 'w')
    return mi_archivo.write('contenido eliminado')


''' 
Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y 
lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.
'''


def registro_error(archivo):
    mi_archivo = open(archivo, 'a')
    mi_archivo.write('se ha registrado un error de ejecución')
    mi_archivo.close()
