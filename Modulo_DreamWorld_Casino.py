# Importamos la función mostrar_menu() desde el archivo principal.
from primerAvance_Grupo08 import usuarios_registrados

def dreamworld_casino():
    # Cargamos la información de los usuarios registrados desde un archivo de texto.
    usuarios = cargar_usuarios()
    # Verificamos que exista al menos un usuario registrado.
    if len(usuarios) == 0:
        print("No hay usuarios registrados. Volviendo al menú principal.")
        mostrar_menu()
        return
    # Autenticamos al usuario.
    id_usuario = autenticar_usuario(usuarios)
    if id_usuario is None:
        print("Se excedió el máximo de intentos para ingresar su ID o PIN, volviendo al menú principal")
        mostrar_menu()
        return
    # Mostramos el mensaje de bienvenida y el submenú.
    print("Bienvenido, {}.".format(id_usuario))
    while True:
        print("1. Retirar dinero")
        print("2. Depositar dinero")
        print("3. Ver saldo actual")
        print("4. Juegos en línea")
        print("5. Eliminar usuario")
        print("6. Salir")
        opcion = input("Ingrese el número de opción: ")
        if opcion == "1":
            retirar_dinero(id_usuario)
        elif opcion == "2":
            depositar_dinero(id_usuario)
        elif opcion == "3":
            ver_saldo(id_usuario)
        elif opcion == "4":
            juegos_en_linea(id_usuario)
        elif opcion == "5":
            eliminar_usuario(id_usuario)
            break
        elif opcion == "6":
            break
    mostrar_menu()

def cargar_usuarios():
    # Implementa esta función para cargar la información de los usuarios registrados desde un archivo de texto.
    pass

def autenticar_usuario(usuarios):
    # Implementa esta función para autenticar al usuario solicitando su ID y PIN.
    pass

def retirar_dinero(id_usuario):
    # Implementa esta función para permitir al usuario retirar dinero de su cuenta.
    pass

def depositar_dinero(id_usuario):
    # Implementa esta función para permitir al usuario depositar dinero en su cuenta.
    pass

def ver_saldo(id_usuario):
    # Implementa esta función para mostrar el saldo actual del usuario.
    pass

def juegos_en_linea(id_usuario):
    # Implementa esta función para permitir al usuario jugar en línea.
    pass

def eliminar_usuario(id_usuario):
    # Implementa esta función para permitir al usuario eliminar su cuenta.
    pass
