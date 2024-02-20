class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    # para querer como se me va a mostrar en pantalla
    def __str__(self):
        return f'Album: {self.titulo}, de {self.autor}'

    # para mostrar el largo
    def __len__(self):
        return self.canciones

    # para eliminar el album
    def __del__(self):
        print('se borro correcta,ente')


mi_cd = CD('Los tigres', 'la bala', 30)

print(mi_cd)
print(len(mi_cd))

# del mi_cd
