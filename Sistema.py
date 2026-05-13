
from Piloto import Piloto
from Equipo import Equipo
from Circuito import Circuito
from Registro import Registro

class Sistema:
    def __init__(self):
        self.__pilotos = []
        self.__equipos = []
        self.__circuitos = []
        self.__cargar_datos()

    def cargar_desde_json(self, gestor_json):
        
        circuitos = gestor_json.cargar_circuitos()
        equipos = gestor_json.cargar_equipos()

        equipos_dict = {e.get_nombre(): e for e in equipos}
        pilotos = gestor_json.cargar_pilotos(equipos_dict=equipos_dict)

        for piloto in pilotos:
            equipo = piloto.get_equipo()
            if equipo and piloto not in equipo.get_pilotos():
                equipo.agregar_piloto(piloto)

        circuitos_dict = {c.get_nombre(): c for c in circuitos}
        pilotos_dict = {p.get_nombre(): p for p in pilotos}
        registros = gestor_json.cargar_registros(
            pilotos_dict=pilotos_dict,
            circuitos_dict=circuitos_dict
        )

        for piloto in pilotos:
            piloto.get_registros().clear()

        for registro in registros:
            registro.get_piloto().agregar_registro(registro)

        self.__circuitos = circuitos
        self.__equipos = equipos
        self.__pilotos = pilotos

        print("\n[OK] Datos cargados desde JSON en memoria.")

    def __cargar_datos(self):
        equipo1 = Equipo("Speed Stars")
        equipo2 = Equipo("Mountain Racers")
        self.__equipos.extend([equipo1, equipo2])

        nombres = ["Akina", "Akagi", "Myogi", "Irohazaka", "Paluato"]
        for n in nombres:
            self.__circuitos.append(Circuito(n, "Montaña"))

        nombres_pilotos = [
            ("Takumi", 18, "123456", equipo1),
            ("Ryosuke", 22, "789012", equipo2),
            ("Diomedes Diaz", 30, "345678", equipo1),
            ("Silvestre Dangond", 28, "901234", equipo2),
            ("Martin Elias", 26, "567890", equipo1),
            ("Poncho Zuleta", 35, "123456", equipo2)
        ]

        for nombre, edad, cedula, equipo in nombres_pilotos:
            p = Piloto(nombre, edad, cedula, equipo)
            equipo.agregar_piloto(p)
            self.__pilotos.append(p)

        for piloto in self.__pilotos:
            for circuito in self.__circuitos:
                tiempo = round(4.0 + (hash(piloto.get_nombre() + circuito.get_nombre()) % 100) / 100, 2)
                r = Registro(piloto, circuito, tiempo)
                piloto.agregar_registro(r)

    def mostrar_pilotos(self):
        for p in self.__pilotos:
            p.mostrar_info()

    def buscar_piloto(self, nombre):
        for p in self.__pilotos:
            if p.get_nombre().lower() == nombre.lower():
                p.mostrar_info()
                return
        print("Piloto no encontrado")

    def mostrar_circuitos(self):
        for c in self.__circuitos:
            c.mostrar()

    def agregar_piloto(self, nombre, edad, cedula, nombre_equipo):
        nombre = nombre.strip()
        cedula = cedula.strip()
        if not nombre:
            print("\n[!] Error: El nombre del piloto no puede estar vacío.")
            return
        if any(caracter.isdigit() for caracter in nombre):
            print(f"\n[!] Error: El nombre '{nombre}' no puede contener números.")
            return
        if not cedula:
            print("\n[!] Error: La cédula no puede estar vacía.")
            return
        if any(p.get_cedula() == cedula for p in self.__pilotos):
            print(f"\n[!] Error: La cédula '{cedula}' ya está registrada.")
            return
        if edad < 17:
            print(f"\n[!] Error: {nombre} debe tener al menos 18 años.")
            return
        for p in self.__pilotos:
            if p.get_nombre().strip().lower() == nombre.lower():
                print(f"\n[!] Error: El piloto '{nombre}' ya está registrado.")
                return
        equipo_encontrado = 0
        for e in self.__equipos:
            if e.get_nombre().lower() == nombre_equipo.strip().lower():
                equipo_encontrado = e
                break
        if equipo_encontrado:
            nuevo_p = Piloto(nombre, edad, cedula, equipo_encontrado)
            equipo_encontrado.agregar_piloto(nuevo_p)
            self.__pilotos.append(nuevo_p)
            print(f"\n[OK] Piloto '{nombre}' agregado a '{equipo_encontrado.get_nombre()}'.")
        else:
            print(f"\n[!] Error: El equipo '{nombre_equipo}' no existe.")

    def modificar_registro(self, nombre_piloto, nombre_circuito, nuevo_tiempo):
        for p in self.__pilotos:
            if p.get_nombre().lower() == nombre_piloto.strip().lower():
                for reg in p.get_registros():
                    if reg.get_circuito().get_nombre().lower() == nombre_circuito.strip().lower():
                        reg.set_tiempo(nuevo_tiempo)
                        print(f"\n[OK] Tiempo actualizado para {p.get_nombre()} en {reg.get_circuito().get_nombre()}.")
                        return
        print("\n[!] Error: No se encontró un registro previo para esa combinación.")

    def mejor_piloto(self):
        mejor = None
        mejor_tiempo = 999
        for p in self.__pilotos:
            for r in p.get_registros():
                if r.get_tiempo() < mejor_tiempo:
                    mejor_tiempo = r.get_tiempo()
                    mejor = p
        if mejor:
            print(f"Mejor piloto: {mejor.get_nombre()} con tiempo {mejor_tiempo}")

    def mostrar_equipos(self):
        for e in self.__equipos:
            e.mostrar_equipo()

    def registrar_nuevo_tiempo(self, nombre_piloto, nombre_circuito, tiempo):
        piloto_objecto = None
        for p in self.__pilotos:
            if p.get_nombre().lower() == nombre_piloto.strip().lower():
                piloto_objecto = p
                break
        circuito_objecto = None
        for c in self.__circuitos:
            if c.get_nombre().lower() == nombre_circuito.strip().lower():
                circuito_objecto = c
                break
        if piloto_objecto and circuito_objecto:
            nuevo_registro = Registro(piloto_objecto, circuito_objecto, tiempo)
            piloto_objecto.agregar_registro(nuevo_registro)
            print(f"\n[OK] Registro creado: {piloto_objecto.get_nombre()} en {circuito_objecto.get_nombre()} ({tiempo}s)")
        else:
            print("\n[!] Error: No se encontró el piloto o el circuito.")
    
    # Getters para JSON
    def get_pilotos(self):
        return self.__pilotos
    
    def get_equipos(self):
        return self.__equipos
    
    def get_circuitos(self):
        return self.__circuitos        