
import os

from Sistema import Sistema
from Usuario import Usuario, Admin
from Datos_Json import GestorJSON


sistema = Sistema()
gestor = GestorJSON("datos")


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPresiona Enter para continuar...")


def pedir_texto(mensaje, permitir_vacio=False):
    while True:
        valor = input(mensaje).strip()
        if valor or permitir_vacio:
            return valor
        print("El valor no puede estar vacío.")


def pedir_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Debes ingresar un número mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Ingresa un número entero válido.")


def pedir_decimal(mensaje, minimo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Debes ingresar un número mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Ingresa un número decimal válido.")


def mostrar_banner():
    print("=" * 60)
    print("      SISTEMA DE PILOTOS - TERMINAL DE CONTROL      ")
    print("=" * 60)


def guardar_datos():
    gestor.guardar_circuitos(sistema.get_circuitos())
    gestor.guardar_equipos(sistema.get_equipos())
    gestor.guardar_pilotos(sistema.get_pilotos())

    todos_registros = []
    for piloto in sistema.get_pilotos():
        todos_registros.extend(piloto.get_registros())
    if todos_registros:
        gestor.guardar_registros(todos_registros)

try:
    sistema.cargar_desde_json(gestor)
except Exception as e:
    print(f"No fue posible cargar los datos desde JSON al iniciar: {e}")



def iniciar_sesion():
    limpiar_pantalla()
    mostrar_banner()
    for intento in range(3):
        print("\n--- INICIO DE SESIÓN ---")
        print("1. Admin")
        print("2. Usuario")
        inicio = pedir_texto("Seleccione: ")
        if inicio == "1":
            nombre_admin = pedir_texto("Nombre de admin: ")
            contrasena = pedir_texto("Contraseña de admin: ")
            if contrasena == "admin":
                print("Sesión iniciada como admin.")
                admin = Admin(nombre_admin, "total")
                admin.saludar()
                pausar()
                return 'admin'
            else:
                print("Contraseña incorrecta.")
        elif inicio == "2":
            nombre_usuario = pedir_texto("Nombre de usuario: ")
            print("Sesión iniciada como usuario.")
            usuario = Usuario(nombre_usuario)
            usuario.saludar()
            pausar()
            return 'usuario'
        else:
            print("Opción inválida.")
    print("Demasiados intentos. Saliendo...")
    exit()


rol = iniciar_sesion()


def menu_usuario():
    while True:
        limpiar_pantalla()
        mostrar_banner()
        print("\n--- MENÚ USUARIO ---")
        print("1. Mostrar pilotos")
        print("2. Buscar piloto")
        print("3. Mostrar circuitos")
        print("4. Mejor piloto")
        print("5. Mostrar equipos")
        print("6. Salir")

        op = pedir_texto("Seleccione: ")
        if op == "1":
            sistema.mostrar_pilotos()
            pausar()
        elif op == "2":
            nombre = pedir_texto("Nombre: ")
            sistema.buscar_piloto(nombre)
            pausar()
        elif op == "3":
            sistema.mostrar_circuitos()
            pausar()
        elif op == "4":
            sistema.mejor_piloto()
            pausar()
        elif op == "5":
            sistema.mostrar_equipos()
            pausar()
        elif op == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")
            pausar()


def menu_admin():
    while True:
        limpiar_pantalla()
        mostrar_banner()
        print("\n--- MENÚ ADMIN ---")
        print("1. Mostrar pilotos")
        print("2. Buscar piloto")
        print("3. Mostrar circuitos")
        print("4. Agregar piloto")
        print("5. Crear equipo")
        print("6. Crear circuito")
        print("7. Modificar equipo")
        print("8. Modificar circuito")
        print("9. Eliminar piloto")
        print("10. Eliminar equipo")
        print("11. Eliminar circuito")
        print("12. Eliminar tiempo de un piloto")
        print("13. Eliminar todos los tiempos de un piloto")
        print("14. Mejor piloto")
        print("15. Mostrar equipos")
        print("16. Registrar tiempo Nuevo (Carrera)")
        print("17. Modificar tiempo existente")
        print("18. Guardar y salir")

        op = pedir_texto("Seleccione: ")
        if op == "1":
            sistema.mostrar_pilotos()
            pausar()
        elif op == "2":
            nombre = pedir_texto("Nombre: ")
            sistema.buscar_piloto(nombre)
            pausar()
        elif op == "3":
            sistema.mostrar_circuitos()
            pausar()
        elif op == "4":
            nombre = pedir_texto("Nombre: ")
            cedula = pedir_texto("Cédula: ")
            edad = pedir_entero("Edad: Mayor o igual a 18: ", minimo=18)
            print("Equipos disponibles: Speed Stars, Mountain Racers")
            nombre_equipo = pedir_texto("Equipo: ")
            sistema.agregar_piloto(nombre, edad, cedula, nombre_equipo)
            pausar()
        elif op == "5":
            nombre_equipo = pedir_texto("Nombre del nuevo equipo: ")
            sistema.agregar_equipo(nombre_equipo)
            pausar()
        elif op == "6":
            nombre_circuito = pedir_texto("Nombre del nuevo circuito: ")
            tipo_circuito = pedir_texto("Tipo del circuito: ")
            sistema.agregar_circuito(nombre_circuito, tipo_circuito)
            pausar()
        elif op == "7":
            nombre_actual = pedir_texto("Nombre actual del equipo: ")
            nuevo_nombre = pedir_texto("Nuevo nombre del equipo: ")
            sistema.modificar_equipo(nombre_actual, nuevo_nombre)
            pausar()
        elif op == "8":
            nombre_actual = pedir_texto("Nombre actual del circuito: ")
            nuevo_nombre = pedir_texto("Nuevo nombre del circuito (Enter para mantener): ", permitir_vacio=True)
            nuevo_tipo = pedir_texto("Nuevo tipo del circuito (Enter para mantener): ", permitir_vacio=True)
            sistema.modificar_circuito(nombre_actual, nuevo_nombre, nuevo_tipo)
            pausar()
        elif op == "9":
            nombre_piloto = pedir_texto("Nombre del piloto a eliminar: ")
            sistema.eliminar_piloto(nombre_piloto)
            pausar()
        elif op == "10":
            nombre_equipo = pedir_texto("Nombre del equipo a eliminar: ")
            sistema.eliminar_equipo(nombre_equipo)
            pausar()
        elif op == "11":
            nombre_circuito = pedir_texto("Nombre del circuito a eliminar: ")
            sistema.eliminar_circuito(nombre_circuito)
            pausar()
        elif op == "12":
            nombre_piloto = pedir_texto("Nombre del piloto: ")
            nombre_circuito = pedir_texto("Nombre del circuito: ")
            sistema.eliminar_tiempo_piloto(nombre_piloto, nombre_circuito)
            pausar()
        elif op == "13":
            nombre_piloto = pedir_texto("Nombre del piloto: ")
            sistema.eliminar_todos_tiempos_piloto(nombre_piloto)
            pausar()
        elif op == "14":
            sistema.mejor_piloto()
            pausar()
        elif op == "15":
            sistema.mostrar_equipos()
            pausar()
        elif op == "16":
            nombre_piloto = pedir_texto("Nombre del piloto: ")
            nombre_circuito = pedir_texto("Nombre del circuito (Akina, Akagi, Myogi, Irohazaka, Paluato): ")
            nuevo_tiempo = pedir_decimal("Nuevo tiempo: ", minimo=0)
            sistema.registrar_nuevo_tiempo(nombre_piloto, nombre_circuito, nuevo_tiempo)
            pausar()
        elif op == "17":
            nombre_piloto = pedir_texto("Nombre del piloto: ")
            nombre_circuito = pedir_texto("Nombre del circuito (Akina, Akagi, Myogi, Irohazaka, Paluato): ")
            nuevo_tiempo = pedir_decimal("Nuevo tiempo: ", minimo=0)
            sistema.modificar_registro(nombre_piloto, nombre_circuito, nuevo_tiempo)
            pausar()
        elif op == "18":
            try:
                guardar_datos()
                print("Datos guardados. Saliendo...")
            except Exception as e:
                print(f"Error al guardar: {e}")
            break
        else:
            print("Opción inválida")
            pausar()


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