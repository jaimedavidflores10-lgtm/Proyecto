
class Circuito:
    def __init__(self, nombre, tipo):
        self.__nombre = nombre
        self.__tipo = tipo

    def get_nombre(self):
        return self.__nombre
    def get_tipo(self):
        return self.__tipo
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_tipo(self, tipo):
        self.__tipo = tipo

    def mostrar(self):
        print(f"{self.get_nombre()} ({self.get_tipo()})")
