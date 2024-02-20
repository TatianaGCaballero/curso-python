class Animal:
    def __init__(self, edad, color):
        self.color = color
        self.edad = edad

    def nacer(self):
        print('nacio')


class Pajaro(Animal):
    pass


piolin = Pajaro(2, 'rojo')
print(piolin.color)
piolin.nacer()
