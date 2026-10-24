
class Pelicula:
    def __init__(self, titulo, director, genero):
        self.titulo = titulo
        self.director = director
        self.genero = genero

    def resumen(self):
        return f"{self.titulo} es una película dirigida por {self.director} y pertenece al género {self.genero}."
