# metodos de instancia

class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio')

    def volar(self, metros):
        print(f'el pajaro vuela {metros} metros')

    # se puede modifcar metodos de instancia
    def pintar_negro(self):
        self.color = 'rosa'
        print(f'ahora el pajaro es {self.color}')


piolin = Pajaro('amarillo', 'tucam')

print(piolin.color)
print(piolin.especie)
piolin.volar(50)
piolin.piar()
piolin.pintar_negro()
# se puede modificar atributos de instancia
piolin.alas = False
print(piolin.alas)


# metodos de clase

class Pajaro:
    alas = True

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'la cantidad de huevos son {cantidad}')
        # se puede modificar atributos de clase
        cls.alas = False
        print(Pajaro.alas)


Pajaro.poner_huevos(30)


# metodos estaticos
class Pajaro:
    @staticmethod
    def mirar():
        print('el pajaro mira')


Pajaro.mirar()
