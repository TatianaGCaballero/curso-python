import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')
# ver texto en string
# print(resultado.text)

# para verlo sin string

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
# print(sopa)

# para ver cual etiqueta quiero mostrar

print(sopa.select('title'))


# para ver etiqueta sulta

print(sopa.select('title')[0])

# soo para ver el titulo
print(sopa.select('title')[0].getText())

# extraer elementos de clase

# columna_lateral = sopa.select('.widget-content')
# print(columna_lateral)

# extraer una imagen
resultado = requests.get('https://www.escueladirecta.com/courses')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
# imagenes = sopa.select('img')


# for i in imagenes:
    # print(i)

imagenes = sopa.select('.course-box-image')
print(imagenes)

imagen_curso_1 = requests.get('https://process.fs.teachablecdn.com/ADNupMnWyR7kCWRvm76Laz/resize=width:705/https://file-uploads.teachablecdn.com/136becbcea3e4d51abede23bf9794cf1/bcae2c4d38ac4953bd27a3d3be140893')

f = open('mi_imagen.jpg','wb')
f.write(imagen_curso_1.content)
f.close()