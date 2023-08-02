# Función para cargar la información de usuarios desde un archivo de texto
def cargar_usuarios():
    try:
        with open("usuarios.txt", "r") as file:
            usuarios = [line.strip().split(",") for line in file.readlines()]
        return usuarios
    except FileNotFoundError:
        print("¡Archivo de usuarios no encontrado!")
        return []

# Función para buscar un usuario por ID y autenticarlo con el PIN
def autenticar_usuario(usuarios):
    max_intentos = 3
    while max_intentos > 0:
        input_id = input("Ingrese su ID: ")
        input_pin = input("Ingrese su PIN: ")

        for usuario in usuarios:
            if usuario[0] == input_id and usuario[1] == input_pin:
                return usuario[2]  

        max_intentos -= 1
        if max_intentos > 0:
            print(f"Credenciales inválidas. Le quedan {max_intentos} intentos.")
        else:
            print("Se excedió el máximo de intentos para ingresar su PIN.")
            return None

# Función mostrar el menú principal y el submenú
def mostrar_menu_principal():
    usuarios = cargar_usuarios()

    if not usuarios:
        print("No hay usuarios registrados. Cerrando el programa.")
        return

    nombre_usuario = autenticar_usuario(usuarios)
    if not nombre_usuario:
        return

    print(f"Bienvenido, {nombre_usuario}.")

    while True:
        print("\n=== Menú ===")
        print("1. Retirar dinero")
        print("2. Depositar dinero")
        print("3. Ver saldo actual")
        print("4. Juegos en línea")
        print("5. Eliminar usuario")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")
        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    mostrar_menu_principal()
