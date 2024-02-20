def suma():
    n1 = int(input('numero1: '))
    n2 = int(input('numero2: '))

    print(n1 + n2)
    print('gracias')


suma()
try:
    suma()

except:
    print('algo ha salido mal')
else:
    print('hiciste tod bien')

finally:
    print('eso fue todo')


# 2 forma

def suma():
    n1 = int(input('numero1: '))
    n2 = int(input('numero2: '))

    print(n1 + n2)
    print('gracias')


try:
    suma()
except TypeError:
    print('estas intentando concatenar diferentes tipos')
except ValueError:
    print('eso no es un numero')


# 3 forma

def pedir_numero():
    while True:
        try:
            numero = int('dame tu numero: ')
        except:
            print('ese no es un numero')

        else:
            print(f'ingresaste el numero {numero}')
            break
        print('gracias')


pedir_numero()

# 4 forma

def suma(num1,num2):
    try:
        print(num1+num2)
    except:
        print("Error inesperado")
