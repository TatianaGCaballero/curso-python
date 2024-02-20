class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

persona_1 = Persona('Tatiana', 25, 'biologa')
persona_2 = Persona('Yeison', 28, 'ingeniero')

print(f'hola soy {persona_1.nombre}, tengo {persona_1.edad} años y soy {persona_1.profesion}')
print(f'hola soy {persona_2.nombre}, tengo {persona_2.edad} años y soy {persona_2.profesion}')
