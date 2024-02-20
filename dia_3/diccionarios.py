mi_dic = {'c1': 'tati', 'c2': 'gomez'}
print(mi_dic)

resultado = mi_dic['c1']
print(resultado)

# segundo

cliente = {'nombre': 'tati',
           'apellido': 'gomez',
           'edad': 25,
           }


consulta = cliente['apellido']
print(consulta)

dic = {'c1': 55,
       'c2': [10, 12, 15],
       'c3': {'s1': 100, 's2': 345}
       }

print(dic['c2'][1])
print(dic['c3']['s2'])

# 3 caso

dict_2 = {'c1': ['a','b','c'],
          'c2': ['d','e','f']
}

# vuelva mayuscula la d

resultado = dict_2['c2'][0].upper()
print(resultado)

# a;adir

dict_2['c3'] = ['g']
print(dict_2)

# reemplazar

dict_2['c1'][1] = 'B'
print(dict_2)

