# Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc.

mi_lista = ['tati', 'yei', True,5,6,'biologa']
print(mi_lista)

# Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:


medios_transporte = ["avión", "auto", "barco", "bicicleta"]

medios_transporte.append('motocicleta')
print(medios_transporte)


'''
Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, 
y almacénalo en una variable llamada eliminado. Utiliza métodos de listas sin alterar 
la línea de código ya suministrada.
'''

frutas = ['manzana', 'fresa', 'pitaya', 'arandanos', 'papaya']
eliminado = frutas.pop(2)
print(eliminado)

print(frutas)