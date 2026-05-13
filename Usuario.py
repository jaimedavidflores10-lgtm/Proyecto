
class Usuario:
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def get_nombre(self):
        return self.__nombre    

    def mostrar(self):
        print(f"Usuario: {self.__nombre}")

    def saludar(self):
        print(f"¡Hola, {self.__nombre}! Bienvenido al sistema de pilotos.")    

class Admin(Usuario):
    def __init__(self, nombre, nivel_acceso):
        super().__init__(nombre)
        self.__nivel_acceso = nivel_acceso

    def get_nivel_acceso(self):
        return self.__nivel_acceso

    def mostrar(self):
        super().mostrar()
        print(f"Nivel de acceso: {self.__nivel_acceso}")

    def saludar(self):
        print(f"¡Hola, {self.get_nombre()}! Eres un administrador con nivel de acceso {self.__nivel_acceso}.")   

class Invitado(Usuario):
    def __init__(self, nombre, fecha_visita):
        super().__init__(nombre)
        self.__fecha_visita = fecha_visita

    def get_fecha_visita(self):
        return self.__fecha_visita

    def mostrar(self):
        super().mostrar()
        print(f"Fecha de visita: {self.__fecha_visita}")        

    def saludar(self):
        print(f"¡Hola, {self.get_nombre()}! Eres un invitado que visitó el sistema el {self.__fecha_visita}.")   