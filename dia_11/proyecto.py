import bs4
import requests

# explorar multiples paginas
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

for n in range(1,11):
    print(url_base.format(n))

# identiicar condiciones de extraccion

resultado = requests.get(url_base.format(1))
sopa = bs4.BeautifulSoup(resultado.text,'lxml')
print(sopa.select('.product_pod'))

# extraer el titulo del libro

libros = sopa.select('.product_pod')
# para sacar los lobros con tres estrellas
ejemplo = libros[0].select('.star-rating.Three')
print(ejemplo)
# para sacar el titulo
ejemplo_2 = libros[0].select('a')[1]['title']
print(ejemplo_2)