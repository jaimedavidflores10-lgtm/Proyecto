
from Sistema import Sistema
from Usuario import Usuario, Admin
from Datos_Json import GestorJSON


sistema = Sistema()
gestor = GestorJSON("datos")  # Crear gestor JSON


def guardar_datos():
    gestor.guardar_circuitos(sistema.get_circuitos())
    gestor.guardar_equipos(sistema.get_equipos())
    gestor.guardar_pilotos(sistema.get_pilotos())

    todos_registros = []
    for piloto in sistema.get_pilotos():
        todos_registros.extend(piloto.get_registros())
    if todos_registros:
        gestor.guardar_registros(todos_registros)

# Si ya existen archivos JSON, cargar su contenido en memoria al iniciar.
try:
    sistema.cargar_desde_json(gestor)
except Exception as e:
    print(f"No fue posible cargar los datos desde JSON al iniciar: {e}")



def iniciar_sesion():
    for intento in range(3):
        print("\n--- INICIO DE SESIÓN ---")
        print("1. Admin")
        print("2. Usuario")
        inicio = input("Seleccione: ")
        if inicio == "1":
            nombre_admin = input("Nombre de admin: ")
            contrasena = input("Contraseña de admin: ")
            if contrasena == "admin":
                print("Sesión iniciada como admin.")
                admin = Admin(nombre_admin, "total")
                admin.saludar()
                return 'admin'
            else:
                print("Contraseña incorrecta.")
        elif inicio == "2":
            nombre_usuario = input("Nombre de usuario: ")
            print("Sesión iniciada como usuario.")
            usuario = Usuario(nombre_usuario)
            usuario.saludar()
            return 'usuario'
        else:
            print("Opción inválida.")
    print("Demasiados intentos. Saliendo...")
    exit()


rol = iniciar_sesion()


def menu_usuario():
    while True:
        print("\n--- MENÚ USUARIO ---")
        print("1. Mostrar pilotos")
        print("2. Buscar piloto")
        print("3. Mostrar circuitos")
        print("4. Mejor piloto")
        print("5. Mostrar equipos")
        print("6. Salir")

        op = input("Seleccione: ")
        if op == "1":
            sistema.mostrar_pilotos()
        elif op == "2":
            nombre = input("Nombre: ")
            sistema.buscar_piloto(nombre)
        elif op == "3":
            sistema.mostrar_circuitos()
        elif op == "4":
            sistema.mejor_piloto()
        elif op == "5":
            sistema.mostrar_equipos()
        elif op == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")


def menu_admin():
    while True:
        print("\n--- MENÚ ADMIN ---")
        print("1. Mostrar pilotos")
        print("2. Buscar piloto")
        print("3. Mostrar circuitos")
        print("4. Agregar piloto")
        print("5. Mejor piloto")
        print("6. Mostrar equipos")
        print("7. Registrar tiempo Nuevo (Carrera)")
        print("8. Modificar tiempo existente")
        print("9. Guardar y salir")

        op = input("Seleccione: ")
        if op == "1":
            sistema.mostrar_pilotos()
        elif op == "2":
            nombre = input("Nombre: ")
            sistema.buscar_piloto(nombre)
        elif op == "3":
            sistema.mostrar_circuitos()
        elif op == "4":
            nombre = input("Nombre: ")
            cedula = input("Cédula: ")
            try:
                edad = int(input("Edad: Mayor o igual a 18: "))
            except ValueError:
                print("Edad inválida.")
                continue
            print("Equipos disponibles: Speed Stars, Mountain Racers")
            nombre_equipo = input("Equipo: ")
            sistema.agregar_piloto(nombre, edad, cedula, nombre_equipo)
        elif op == "5":
            sistema.mejor_piloto()
        elif op == "6":
            sistema.mostrar_equipos()
        elif op == "7":
            nombre_piloto = input("Nombre del piloto: ")
            nombre_circuito = input("Nombre del circuito(Akina, Akagi, Myogi, Irohazaka, Paluato): ")
            try:
                nuevo_tiempo = float(input("Nuevo tiempo: "))
                sistema.registrar_nuevo_tiempo(nombre_piloto, nombre_circuito, nuevo_tiempo)
            except ValueError:
                print("Tiempo inválido. Debe ser un número(Decimal).")
        elif op == "8":
            nombre_piloto = input("Nombre del piloto: ")
            nombre_circuito = input("Nombre del circuito(Akina, Akagi, Myogi, Irohazaka, Paluato): ")
            try:
                nuevo_tiempo = float(input("Nuevo tiempo: "))
                sistema.modificar_registro(nombre_piloto, nombre_circuito, nuevo_tiempo)
            except ValueError:
                print("Tiempo inválido. Debe ser un número(Decimal).")
        elif op == "9":
            try:
                guardar_datos()
                print("Datos guardados. Saliendo...")
            except Exception as e:
                print(f"Error al guardar: {e}")
            break
        else:
            print("Opción inválida")


try:
    if rol == 'admin':
        menu_admin()
    else:
        menu_usuario()
finally:
    try:
        guardar_datos()
        print("Datos guardados automáticamente al cerrar el programa.")
    except Exception as e:
        print(f"No fue posible guardar automáticamente al cerrar: {e}")