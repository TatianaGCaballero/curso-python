'''
Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla "¡Hola mundo!"

Solo debes definir la función, no debes invocarla luego.
'''

def funcion():
    print('holiii')

funcion()

'''
Declara una función llamada bienvenida, que tome como argumento el nombre de una persona, 
y que cada vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!"

Crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.
'''


def bienvenido(nombre):
    print(f'holi {nombre}')


bienvenido('tati')

'''
Declara una función llamada cuadrado, que tome como argumento un número cualquiera, 
y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número (
es decir, la potencia 2 del valor).

El nombre del argumento que debe tomar dicha función es un_numero. 
Crea dicha variable y asígnale un número cualquiera.
'''

numero = 6


def cuadrado (numero):
    print(numero**2)


cuadrado(numero)

'''
Crea una función llamada potencia que tome dos valores numéricos como argumentos. 
Deberá devolver el número que resulte de resolver una potencia, utilizando el primer número como base, 
y el segundo como exponente:
'''


def potencia(num1, num2):
    total = num1 ** num2
    return total


resultado = potencia(3,6)
print(resultado)

'''
Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico 
(un monto en dólares estadounidenses), y devuelva como resultado el monto equivalente en euros. 
A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.

Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu 
función y evaluar su resultado.
'''

dolares = 500

def conversion(dolares):
    total = dolares * 0.90
    return total

resultado = conversion(dolares)
print(resultado)

'''
Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, 
invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.

Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"

También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, 
para sumisitrarle como argumento a la función creada
'''

palabra = 'python'
def invertir(palabra):
    total = palabra[::-1]
    return total

resultado = invertir(palabra)
print(resultado)