import json
import os
from Circuito import Circuito
from Piloto import Piloto
from Equipo import Equipo
from Registro import Registro


class GestorJSON:
    """Clase para gestionar la lectura y escritura de datos en archivos JSON"""
    
    def __init__(self, carpeta_datos="datos"):
        
        base_dir = os.path.dirname(__file__)
        if not os.path.isabs(carpeta_datos):
            carpeta_datos = os.path.join(base_dir, carpeta_datos)

        self.carpeta_datos = carpeta_datos

        
        if not os.path.exists(self.carpeta_datos):
            os.makedirs(self.carpeta_datos)
    
    def guardar_circuitos(self, circuitos, nombre_archivo="circuitos.json"):
        
        ruta = os.path.join(self.carpeta_datos, nombre_archivo)
        datos = []
        
        for circuito in circuitos:
            datos.append({
                "nombre": circuito.get_nombre(),
                "tipo": circuito.get_tipo()
            })
        
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        
        print(f"[OK] {len(circuitos)} circuito(s) guardado(s) en {ruta}")
    
    def cargar_circuitos(self, nombre_archivo="circuitos.json"):
        
        ruta = os.path.join(self.carpeta_datos, nombre_archivo)
        
        if not os.path.exists(ruta):
            print(f"El archivo {ruta} no existe")
            return []
        
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            circuitos = []
            for item in datos:
                circuito = Circuito(item['nombre'], item['tipo'])
                circuitos.append(circuito)
            
            print(f"{len(circuitos)} circuito(s) cargado(s) desde {ruta}")
            return circuitos
        
        except Exception as e:
            print(f"Error al cargar circuitos: {e}")
            return []
    
    def guardar_equipos(self, equipos, nombre_archivo="equipos.json"):
        
        ruta = os.path.join(self.carpeta_datos, nombre_archivo)
        datos = []
        
        for equipo in equipos:
            datos.append({
                "nombre": equipo.get_nombre(),
                "pilotos": [p.get_nombre() for p in equipo.get_pilotos()]
            })
        
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        
        print(f"[OK] {len(equipos)} equipo(s) guardado(s) en {ruta}")
    
    def cargar_equipos(self, nombre_archivo="equipos.json"):
        
        ruta = os.path.join(self.carpeta_datos, nombre_archivo)
        
        if not os.path.exists(ruta):
            print(f"[!] El archivo {ruta} no existe")
            return []
        
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            equipos = []
            for item in datos:
                equipo = Equipo(item['nombre'])
                equipos.append(equipo)
            
            print(f"[OK] {len(equipos)} equipo(s) cargado(s) desde {ruta}")
            return equipos
        
        except Exception as e:
            print(f"[ERROR] Error al cargar equipos: {e}")
            return []
    
    def guardar_pilotos(self, pilotos, nombre_archivo="pilotos.json"):
         
        ruta = os.path.join(self.carpeta_datos, nombre_archivo)
        datos = []
        
        for piloto in pilotos:
            datos.append({
                "nombre": piloto.get_nombre(),
                "edad": piloto.get_edad(),
                "cedula": piloto.get_cedula(),
                "equipo": piloto.get_equipo().get_nombre() if piloto.get_equipo() else None,
                "registros": [
                    {
                        "circuito": r.get_circuito().get_nombre(),
                        "tiempo": r.get_tiempo()
                    }
                    for r in piloto.get_registros()
                ]
            })
        
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        
        print(f"[OK] {len(pilotos)} piloto(s) guardado(s) en {ruta}")
    
    def cargar_pilotos(self, equipos_dict=None, nombre_archivo="pilotos.json"):

        ruta = os.path.join(self.carpeta_datos, nombre_archivo)
        
        if not os.path.exists(ruta):
            print(f"[!] El archivo {ruta} no existe")
            return []
        
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            pilotos = []
            for item in datos:
                # Buscar el equipo en el diccionario
                equipo = None
                if equipos_dict and item['equipo'] in equipos_dict:
                    equipo = equipos_dict[item['equipo']]
                
                piloto = Piloto(item['nombre'], item['edad'], item['cedula'], equipo)
                pilotos.append(piloto)
            
            print(f"{len(pilotos)} piloto(s) cargado(s) desde {ruta}")
            return pilotos
        
        except Exception as e:
            print(f"Error al cargar pilotos: {e}")
            return []
    
    def guardar_registros(self, registros, nombre_archivo="registros.json"):
        
        ruta = os.path.join(self.carpeta_datos, nombre_archivo)
        datos = []
        
        for registro in registros:
            datos.append({
                "piloto": registro.get_piloto().get_nombre(),
                "circuito": registro.get_circuito().get_nombre(),
                "tiempo": registro.get_tiempo()
            })
        
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        
        print(f"[OK] {len(registros)} registro(s) guardado(s) en {ruta}")
    
    def cargar_registros(self, pilotos_dict=None, circuitos_dict=None, nombre_archivo="registros.json"):
        
        ruta = os.path.join(self.carpeta_datos, nombre_archivo)
        
        if not os.path.exists(ruta):
            print(f"El archivo {ruta} no existe")
            return []
        
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            registros = []
            for item in datos:
                piloto = None
                circuito = None
                
                if pilotos_dict and item['piloto'] in pilotos_dict:
                    piloto = pilotos_dict[item['piloto']]
                
                if circuitos_dict and item['circuito'] in circuitos_dict:
                    circuito = circuitos_dict[item['circuito']]
                
                if piloto and circuito:
                    registro = Registro(piloto, circuito, item['tiempo'])
                    registros.append(registro)
            
            print(f"{len(registros)} registro(s) cargado(s) desde {ruta}")
            return registros
        
        except Exception as e:
            print(f"Error al cargar registros: {e}")
            return []
    
    def ver_contenido_json(self, nombre_archivo):
       
        ruta = os.path.join(self.carpeta_datos, nombre_archivo)
        
        if not os.path.exists(ruta):
            print(f" El archivo {ruta} no existe")
            return
        
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            print(f"\n{'='*50}")
            print(f"Contenido de {nombre_archivo}:")
            print(f"{'='*50}")
            print(json.dumps(datos, indent=4, ensure_ascii=False))
            print(f"{'='*50}\n")
        
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
    
    def limpiar_datos(self):
        """Elimina todos los archivos JSON de la carpeta datos"""
        if os.path.exists(self.carpeta_datos):
            for archivo in os.listdir(self.carpeta_datos):
                if archivo.endswith('.json'):
                    ruta = os.path.join(self.carpeta_datos, archivo)
                    os.remove(ruta)
                    print(f"Eliminado: {archivo}")
