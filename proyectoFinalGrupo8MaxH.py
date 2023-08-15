#Se requiere desarrollar la arquitectura y diseño de un software para el manejo de un casino online, que sea accesible y cuente con medidas de seguridad para proteger el dinero de los usuarios, una plataforma de registro de usuarios, juegos en línea y acceso para configuración del sistema.
#Autores: Max Hernández Medrano, Jose David Jiménez Corrales, Luis Felipe Cabalceta Barrantes.
#05/06/2023. Última actualización: 14/08/2023

#Importamos la biblioteca getpass para la verificación de PIN.
import getpass
import os

#Definimos la variable global usuarios_registrados para almacenar la lista de usuarios registrados durante toda la ejecución del programa.
usuariosRegistrados = []

#Definimos la función nuevoUsuario para llamar al bloque de código que compone la creación de un nuevo usuario.
#Generamos un ciclo while para verificar la cantidad de intentos del usuario para elegir su id y definimos la constante intentos = 3.
#Utilizamos la función len para extraer la cantidad de carácteres requeridos y que cumpla con los requerimientos del sistema.
#A través de estructuras de decisión definimos las condiciones de verificación para continuar con el siguiente paso, elección del PIN de seguridad.      
def nuevoUsuario():
    print("Registro de Nuevo Usuario")
    intentos = 3
    usuariosRegistrados = []
    while intentos > 0:
        idUsuario = input("Ingrese su ID de Usuario (Mínimo 5 caracteres alfanuméricos): \n")
        if len(idUsuario) < 5:
            intentos -= 1
            print("El ID ingresado es demasiado corto. Intentos restantes: {}".format(intentos))
        elif idUsuario in usuariosRegistrados:
            intentos -= 1
            print("El ID {} ya está registrado. Intentos restantes: {}".format(idUsuario, intentos))
        else:
            break
        
#Definimos que cuando el contador de intentos llega a 0, se regresa al menú principal.       
    if intentos == 0:
            print("Se excedió el máximo de intentos para ingresar un ID válido, volviendo al menú principal")
            mostrarMenu()
#Realizamos la elección del PIN de seguridad. Definimos la condición de caracteres a través de if. Nuevamente utilizamos la función len para extraer la cantidad de objetos que requerimos.
#Llamamos a la biblioteca getpass. Realizamos la verificación del pin a través de if para mostrar mensaje a usuario de PIN Registrado correctamente.
    else:
        # Solicitsmos al usuario que ingrese un nombre para mostarse.
        nombreUsuario = input("Ingrese un nombre,para mostrarse\n")
        while True:
            pin = getpass.getpass("Ingrese su PIN de seguridad de 6 dígitos")
            if len(pin) != 6:
                print("El pin ingresado no es válido")
            else:
                confirmacionPin = getpass.getpass("Ingrese nuevamente su PIN de seguridad: ")
                if pin == confirmacionPin:
                    print("PIN registrado con éxito.")
                    #Agregamos el ID y el nombre del usuario a la lista global usuarios_registrados.
                    usuariosRegistrados.append((idUsuario, nombreUsuario))
                    informacion = "Usuario{}, Pin {}".format(idUsuario, pin)
                    try:
                        file = open("usuariosPines.txt", "w") #Creamos el archivo para guardar el usuario.
                        file.write(informacion + "\n") #Abrimos el archivo para escribir nueva información en él.
                        file.close() #Cerramos el archivo.
                    except:
                        print("Archivo no creado")
                    #llamamos a la funcion deposito_minimo() para solicitar al usuario que realice un deposito minimo
                    depositoMinimo()
                    
                    break
                else:
                    print("El PIN de confirmación no coincide. Por favor, ingrese nuevamente el PIN.")

def depositoMinimo():
    #definimos el monto del deposito minimo, en este caso sera de $1500
    montoMinimo = 1500
    #definimos los tipo de cambio
    tipoCambioColones = 600
    tipoCambioBitcoin = 50000
    intentos = 3
    while intentos > 0:
        print("DreamWorld Casino es un casino de alta gama. Para completar el registro, debe realizar un depósito mínimo de ${}.".format(montoMinimo))
        print("Puede realizar el depósito en dólares, colones o bitcoin.")
        moneda = input("Digite el número de la moneda en la que desea realizar el depósito (1. Dólares, 2. Colones o 3. Bitcoin): ")
        monto = float(input("Ingrese el monto que desea depositar: "))
        if moneda == "2":
            monto /= tipoCambioColones
        elif moneda == "3":
            monto *= tipoCambioBitcoin
        if monto >= montoMinimo:
            print("Depósito realizado con éxito. Su cuenta ahora tiene un saldo de ${}.".format(monto))
            #Llamamos a la función mostrarMenu() para volver a mostrar el menú después de realizar el depósito con éxito.
            mostrarMenu()
            break
        else:
            intentos -= 1
            print("El monto depositado no alcanza el mínimo requerido. Intentos restantes: {}".format(intentos))
    if intentos == 0:
        print("Se excedió el máximo de intentos para depositar el mínimo de dinero requerido, volviendo al menú principal")
        mostrarMenu()

     
#Definimos las funciones dreamWorldCasino(), configuracionAvanzada() y salir() como funciones vacías por ahora, para evitar errores a la hora de llamarlas.
def dreamWorldCasino():
    # Cargamos la información de los usuarios registrados desde un archivo de texto.
    usuarios = cargarUsuarios()
    # Verificamos que exista al menos un usuario registrado.
    if len(usuarios) == 0:
        print("No hay usuarios registrados. Volviendo al menú principal.")
        mostrarMenu()
        return
    # Autenticamos al usuario.
    idUsuario = autenticarUsuario(usuarios)
    if idUsuario is None:
        print("Se excedió el máximo de intentos para ingresar su ID o PIN, volviendo al menú principal")
        mostrarMenu()
        return
    # Mostramos el mensaje de bienvenida y el submenú.
    print("Bienvenido, {}.".format(idUsuario))
    while True:
        print("1. Retirar dinero")
        print("2. Depositar dinero")
        print("3. Ver saldo actual")
        print("4. Juegos en línea")
        print("5. Eliminar usuario")
        print("6. Salir")
        opcion = input("Ingrese el número de opción: ")
        if opcion == "1":
            retirarDinero(idUsuario)
        elif opcion == "2":
            depositarDinero(idUsuario)
        elif opcion == "3":
            verSaldo(idUsuario)
        elif opcion == "4":
            juegosEnLinea(idUsuario)
        elif opcion == "5":
            eliminarUsuario(idUsuario)
            break
        elif opcion == "6":
            break
    mostrarMenu()

def cargarUsuarios():
    try:
        with open("usuariosPines.txt", "r") as file:
            usuarios = [line.strip().split(",") for line in file.readlines()]
        return usuarios
    except FileNotFoundError:
        print("¡Archivo de usuarios no encontrado!")
        return []

# Función para buscar un usuario por ID y autenticarlo con el PIN
def autenticarUsuario(usuarios):
    maxIntentos = 3
    while maxIntentos > 0:
        inputId = input("Ingrese su ID: ")
        inputPin = input("Ingrese su PIN: ")

        for usuario in usuarios:
            if usuario[0] == inputId and usuario[1] == inputPin:
                return usuario[2]  

        maxIntentos -= 1
        if maxIntentos > 0:
            print(f"Credenciales inválidas. Le quedan {max_intentos} intentos.")
        else:
            print("Se excedió el máximo de intentos para ingresar su PIN.")
            return None


def retirarDinero(idUsuario):
    #Seccion en desarrollo.
    pass

def depositarDinero(idUsuario):
    #Seccion en desarrollo.
    pass

def verSaldo(idUsuario):
    #Seccion en desarrollo.
    pass

def juegosEnLinea(id_usuario):
    #Seccion en desarrollo.
    pass

def eliminarUsuario(id_usuario):
    #Seccion en desarrollo.
    pass

def configuracionAvanzada():
    print("Esta sección está en desarrollo.")
    mostrarMenu()


def salir():
    print("Gracias por utilizar DreamWorld Casino. ¡Hasta pronto!")
    
#Creamos el menú principal de nuestro programa. 
#Utilizamos la función def() para definir mostrarMenu como la función para mostrar en pantalla el menú al usuario y las 4 secciones que componen el software. 
def mostrarMenu():
    print("Bienvenido a DreamWorld Casino. Por favor, elegí una opción:")
    print("1. Registro de usuario nuevo")
    print("2. DreamWorld Casino")
    print("3. Configuración Avanzada")
    print("4. Salir")

   
#Solicitamos al usuario que ingrese a través de un input la sección a la que desea ingresar. Definimos las condiciones a través de estructuras de decisión (if/elif/else).  
    opcion = input("Ingresa el número de opción: \n")

    if opcion == "1":
        nuevoUsuario()
    elif opcion == "2":
        dreamWorldCasino()
    elif opcion == "3":
        configuracionAvanzada()
    elif opcion == "4":
        salir()
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
mostrarMenu()

