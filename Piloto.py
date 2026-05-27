
class Piloto:
    def __init__(self, nombre, edad, cedula, equipo):
        self.__nombre = nombre
        self.__edad = edad
        self.__cedula = cedula
        self.__equipo = equipo
        self.__registros = []

    def agregar_registro(self, registro):
        self.__registros.append(registro)

    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_cedula(self):
        return self.__cedula
    def get_equipo(self):
        return self.__equipo
    def get_registros(self):
        return self.__registros
    def set_equipo(self, equipo):
        self.__equipo = equipo

    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"Cédula: {self.__cedula}")
        equipo = self.__equipo.get_nombre() if self.__equipo else "Sin equipo"
        print(f"Equipo: {equipo}")
        print("Registros:")
        for r in self.__registros:
            print(f"  Circuito: {r.get_circuito().get_nombre()} - Tiempo: {r.get_tiempo()}")
        print("-" * 30)

    def get_mejor_tiempo(self):
        if not self.__registros:
            return None
        tiempos = [r.get_tiempo() for r in self.__registros if r.get_tiempo() is not None]
        return min(tiempos) if tiempos else None
