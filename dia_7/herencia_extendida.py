class Animal:
    def __init__(self, edad, color):
        self.color = color
        self.edad = edad

    def nacer(self):
        print('nacio')

    def hablar(self):
        print('este pajaro hace pio')


class Pajaro(Animal):
    # se puede modificar un metodo
    def hablar(self):
        print('pio')

    # se puede añadir un nuevo metodo

    def volar(self, metros):
        print(f'el pajaro vuela {metros} metros ')

    # crear atributos
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo


piolin = Pajaro(2, 'rojo', 70)
print(piolin.color)
print(piolin.altura_vuelo)
piolin.nacer()
piolin.hablar()
piolin.volar(45)


# herencia multiple

class Padre:
    def reir(self):
        print('jajajajaaj')


class Madre:
    def hablar(self):
        print('holiiii')


class Hijo(Padre, Madre):
    pass

tati = Hijo()
tati.reir()
tati.hablar()
