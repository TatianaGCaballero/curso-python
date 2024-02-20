def suma(*args):
    total = 0
    for arg in args:
        total = total + arg
    return total


resultado = suma(3, 4, 5, 6)
print(resultado)


# otra forma
def suma(*args):
    return sum(args)


print(suma(1, 3, 2))


