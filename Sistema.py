
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

    def mostrar_pilotos(self, ordenar_por='nombre'):
        """
        Mostrar pilotos ordenados por 'nombre' o por 'mejor_tiempo'.
        """
        if ordenar_por == 'mejor_tiempo':
            def key_fn(p):
                mejor = p.get_mejor_tiempo()
                return float('inf') if mejor is None else mejor
        else:
            def key_fn(p):
                return p.get_nombre().lower()

        for p in sorted(self.__pilotos, key=key_fn):
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

    def agregar_equipo(self, nombre_equipo):
        nombre_equipo = nombre_equipo.strip()
        if not nombre_equipo:
            print("\n[!] Error: El nombre del equipo no puede estar vacío.")
            return

        for equipo in self.__equipos:
            if equipo.get_nombre().strip().lower() == nombre_equipo.lower():
                print(f"\n[!] Error: El equipo '{nombre_equipo}' ya existe.")
                return

        nuevo_equipo = Equipo(nombre_equipo)
        self.__equipos.append(nuevo_equipo)
        print(f"\n[OK] Equipo '{nombre_equipo}' creado correctamente.")

    def agregar_circuito(self, nombre_circuito, tipo):
        nombre_circuito = nombre_circuito.strip()
        tipo = tipo.strip()

        if not nombre_circuito:
            print("\n[!] Error: El nombre del circuito no puede estar vacío.")
            return
        if not tipo:
            print("\n[!] Error: El tipo de circuito no puede estar vacío.")
            return

        
        tokens = [t for t in nombre_circuito.split() if t]
        if not tokens or not all(t.isalpha() for t in tokens):
            print("\n[!] Error: El nombre del circuito solo puede contener palabras (letras y espacios).")
            return

        for circuito in self.__circuitos:
            if circuito.get_nombre().strip().lower() == nombre_circuito.lower():
                print(f"\n[!] Error: El circuito '{nombre_circuito}' ya existe.")
                return

        nuevo_circuito = Circuito(nombre_circuito, tipo)
        self.__circuitos.append(nuevo_circuito)
        print(f"\n[OK] Circuito '{nombre_circuito}' creado correctamente.")

    def modificar_equipo(self, nombre_actual, nuevo_nombre):
        nombre_actual = nombre_actual.strip()
        nuevo_nombre = nuevo_nombre.strip()

        if not nombre_actual or not nuevo_nombre:
            print("\n[!] Error: Los nombres del equipo no pueden estar vacíos.")
            return

        equipo_objetivo = None
        for equipo in self.__equipos:
            if equipo.get_nombre().strip().lower() == nombre_actual.lower():
                equipo_objetivo = equipo
                break

        if not equipo_objetivo:
            print(f"\n[!] Error: El equipo '{nombre_actual}' no existe.")
            return

        for equipo in self.__equipos:
            if equipo.get_nombre().strip().lower() == nuevo_nombre.lower() and equipo is not equipo_objetivo:
                print(f"\n[!] Error: Ya existe otro equipo con el nombre '{nuevo_nombre}'.")
                return

        equipo_objetivo.set_nombre(nuevo_nombre)
        print(f"\n[OK] Equipo actualizado: '{nombre_actual}' -> '{nuevo_nombre}'.")

    def modificar_circuito(self, nombre_actual, nuevo_nombre=None, nuevo_tipo=None):
        nombre_actual = nombre_actual.strip()
        nuevo_nombre = (nuevo_nombre or "").strip()
        nuevo_tipo = (nuevo_tipo or "").strip()

        if not nombre_actual:
            print("\n[!] Error: El nombre actual del circuito no puede estar vacío.")
            return

        circuito_objetivo = None
        for circuito in self.__circuitos:
            if circuito.get_nombre().strip().lower() == nombre_actual.lower():
                circuito_objetivo = circuito
                break

        if not circuito_objetivo:
            print(f"\n[!] Error: El circuito '{nombre_actual}' no existe.")
            return

        if nuevo_nombre:
            
            tokens = [t for t in nuevo_nombre.split() if t]
            if not tokens or not all(t.isalpha() for t in tokens):
                print("\n[!] Error: El nuevo nombre del circuito solo puede contener palabras (letras y espacios).")
                return
            for circuito in self.__circuitos:
                if circuito.get_nombre().strip().lower() == nuevo_nombre.lower() and circuito is not circuito_objetivo:
                    print(f"\n[!] Error: Ya existe otro circuito con el nombre '{nuevo_nombre}'.")
                    return
            circuito_objetivo.set_nombre(nuevo_nombre)

        if nuevo_tipo:
            circuito_objetivo.set_tipo(nuevo_tipo)

        print(f"\n[OK] Circuito '{nombre_actual}' actualizado correctamente.")

    def eliminar_piloto(self, nombre_piloto):
        nombre_piloto = nombre_piloto.strip()
        if not nombre_piloto:
            print("\n[!] Error: El nombre del piloto no puede estar vacío.")
            return

        piloto_objetivo = None
        for piloto in self.__pilotos:
            if piloto.get_nombre().strip().lower() == nombre_piloto.lower():
                piloto_objetivo = piloto
                break

        if not piloto_objetivo:
            print(f"\n[!] Error: El piloto '{nombre_piloto}' no existe.")
            return

        equipo = piloto_objetivo.get_equipo()
        if equipo and piloto_objetivo in equipo.get_pilotos():
            equipo.get_pilotos().remove(piloto_objetivo)

        self.__pilotos.remove(piloto_objetivo)
        print(f"\n[OK] Piloto '{nombre_piloto}' eliminado correctamente.")

    def eliminar_equipo(self, nombre_equipo):
        nombre_equipo = nombre_equipo.strip()
        if not nombre_equipo:
            print("\n[!] Error: El nombre del equipo no puede estar vacío.")
            return

        equipo_objetivo = None
        for equipo in self.__equipos:
            if equipo.get_nombre().strip().lower() == nombre_equipo.lower():
                equipo_objetivo = equipo
                break

        if not equipo_objetivo:
            print(f"\n[!] Error: El equipo '{nombre_equipo}' no existe.")
            return

    
        pilotos_referenciados = [p for p in self.__pilotos if p.get_equipo() == equipo_objetivo]
        if pilotos_referenciados:
            print(f"\n[!] Error: No se puede eliminar '{nombre_equipo}' porque {len(pilotos_referenciados)} piloto(s) están asignados a este equipo.")
            return

        self.__equipos.remove(equipo_objetivo)
        print(f"\n[OK] Equipo '{nombre_equipo}' eliminado correctamente.")

    def eliminar_circuito(self, nombre_circuito):
        nombre_circuito = nombre_circuito.strip()
        if not nombre_circuito:
            print("\n[!] Error: El nombre del circuito no puede estar vacío.")
            return

        circuito_objetivo = None
        for circuito in self.__circuitos:
            if circuito.get_nombre().strip().lower() == nombre_circuito.lower():
                circuito_objetivo = circuito
                break

        if not circuito_objetivo:
            print(f"\n[!] Error: El circuito '{nombre_circuito}' no existe.")
            return
        registros_referenciados = 0
        for piloto in self.__pilotos:
            for registro in piloto.get_registros():
                if registro.get_circuito() == circuito_objetivo:
                    registros_referenciados += 1
        if registros_referenciados > 0:
            print(f"\n[!] Error: No se puede eliminar '{nombre_circuito}' porque existe(n) {registros_referenciados} registro(s) que lo referencian.")
            return

        self.__circuitos.remove(circuito_objetivo)
        print(f"\n[OK] Circuito '{nombre_circuito}' eliminado correctamente.")

    def eliminar_tiempo_piloto(self, nombre_piloto, nombre_circuito):
        nombre_piloto = nombre_piloto.strip()
        nombre_circuito = nombre_circuito.strip()

        if not nombre_piloto or not nombre_circuito:
            print("\n[!] Error: El nombre del piloto y del circuito no pueden estar vacíos.")
            return

        piloto_objetivo = None
        for piloto in self.__pilotos:
            if piloto.get_nombre().strip().lower() == nombre_piloto.lower():
                piloto_objetivo = piloto
                break

        if not piloto_objetivo:
            print(f"\n[!] Error: El piloto '{nombre_piloto}' no existe.")
            return

        registros = piloto_objetivo.get_registros()
        for registro in list(registros):
            if registro.get_circuito().get_nombre().strip().lower() == nombre_circuito.lower():
                registros.remove(registro)
                print(f"\n[OK] Tiempo eliminado para {nombre_piloto} en {nombre_circuito}.")
                return

        print("\n[!] Error: No se encontró un tiempo para esa combinación.")

    def eliminar_todos_tiempos_piloto(self, nombre_piloto):
        nombre_piloto = nombre_piloto.strip()

        if not nombre_piloto:
            print("\n[!] Error: El nombre del piloto no puede estar vacío.")
            return

        piloto_objetivo = None
        for piloto in self.__pilotos:
            if piloto.get_nombre().strip().lower() == nombre_piloto.lower():
                piloto_objetivo = piloto
                break

        if not piloto_objetivo:
            print(f"\n[!] Error: El piloto '{nombre_piloto}' no existe.")
            return

        cantidad = len(piloto_objetivo.get_registros())
        piloto_objetivo.get_registros().clear()
        print(f"\n[OK] Se eliminaron {cantidad} tiempo(s) del piloto '{nombre_piloto}'.")

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
       
        if not cedula.isdigit():
            print(f"\n[!] Error: La cédula '{cedula}' debe contener solo números.")
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