class Vaca:
    def hablar(self):
        print('la vaca hace muu')


class Oveja:
    def hablar(self):
        print('la oveja hace beeee')


vaca1 = Vaca()
oveja1 = Oveja()

vaca1.hablar()
oveja1.hablar()

# iterar en una lista
animales = [vaca1, oveja1]

for animal in animales:
    animal.hablar()


# funciones
def animal_hablar(animal):
    animal.hablar()


animal_hablar(vaca1)
