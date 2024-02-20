def suma(**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')


suma(x=4, y=6)


def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        total = total + valor
    return total


resultado = suma(x=5, y=5, z=4)
print(resultado)


def prueba(num1, num2, **kwards):
    print(f'el 1 valor es {num1}')
    print(f'el 2 valor es {num2}')

    for clave, valor in kwards.items():
        print(f'{clave} = {valor}')


resultado = prueba(3, 4, x='tati', y=25)
