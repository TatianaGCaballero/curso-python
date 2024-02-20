mi_tuple = (1,2,3,4)
resultado = mi_tuple[0]
print(resultado)

mi_tuple = (1, 'tati', 5.6)
resultado = mi_tuple[1]
print(resultado)

mi_tuple = (1,2,(10,20),4)
resultado = mi_tuple[2][0]
print(resultado)

# count

t = (1,2,3,1)
print(t.index(1))
print(t.count(1))