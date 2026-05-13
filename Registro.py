
class Registro:
    def __init__(self, piloto, circuito, tiempo):
        self.__piloto = piloto
        self.__circuito = circuito
        self.__tiempo = tiempo
    
    def get_piloto(self):
        return self.__piloto
    def get_circuito(self):
        return self.__circuito
    def get_tiempo(self):
        return self.__tiempo
    def set_tiempo(self, tiempo):
        self.__tiempo = tiempo
        

    def mostrar_info(self):
        print(f"Piloto: {self.__piloto.get_nombre()}")
        print(f"Circuito: {self.__circuito.get_nombre()}")
        print(f"Tiempo: {self.__tiempo} segundos")

