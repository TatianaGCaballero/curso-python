# lista de tuplas

nombres = ['ana', 'hugo']
edades = [54,23]

combinar = zip(nombres,edades)
print(list(zip(nombres,edades)))

nombres = ['ana', 'hugo']
edades = [54,23]
for nombre, edad in combinar:
    print(f'{nombre} tiene {edad}')
