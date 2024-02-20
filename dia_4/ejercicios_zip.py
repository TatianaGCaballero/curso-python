'''
Muestra en pantalla frases como la del siguiente ejemplo:

La capital de Alemania es Berlín
'''

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinados = list(zip(capitales,paises))
for capital, pais in combinados:
    print(f'la capital de {pais} es {capital}')

'''
Crea un objeto zip formado a partir de listas, 
de un conjunto de marcas y productos que tú prefieras, dentro de la variable
'''

marcas = ['cyzone', 'avon']
productos = ['perfumes', 'aretes']

mi_zip = zip(marcas,productos)
print(mi_zip)

'''
Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), 
y convierte el objeto generado en una lista almacenada en la variable
'''

espanol = ['uno','dos','tres']

portugues = ['um', 'dois', 'três', 'quatro','cinco']

ingles = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(espanol,portugues,ingles))
print(numeros)