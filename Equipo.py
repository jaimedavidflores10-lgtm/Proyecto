
class Equipo:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__pilotos = []

    def agregar_piloto(self, piloto):
        self.__pilotos.append(piloto)

    def get_nombre(self):
        return self.__nombre

    def get_pilotos(self):
        return self.__pilotos

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def mostrar_equipo(self):
        print(f"Equipo: {self.__nombre}")
        for p in self.__pilotos:
            print(f" - {p.get_nombre()}")
        print("-" * 30)
