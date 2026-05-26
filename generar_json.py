from Sistema import Sistema
from Datos_Json import GestorJSON

print(" GENERANDO ARCHIVOS JSON ")

sistema = Sistema()
gestor = GestorJSON("datos")

print("1. Guardando circuitos...")
gestor.guardar_circuitos(sistema.get_circuitos())

print("2. Guardando equipos...")
gestor.guardar_equipos(sistema.get_equipos())

print("3. Guardando pilotos...")
gestor.guardar_pilotos(sistema.get_pilotos())

print("4. Guardando registros...")
todos_registros = []
for piloto in sistema.get_pilotos():
    todos_registros.extend(piloto.get_registros())
if todos_registros:
    gestor.guardar_registros(todos_registros)

print("Archivos generados exitosamente en la carpeta 'datos'")

print("Archivos creados:")
print("  - datos/circuitos.json")
print("  - datos/equipos.json")
print("  - datos/pilotos.json")
print("  - datos/registros.json")
