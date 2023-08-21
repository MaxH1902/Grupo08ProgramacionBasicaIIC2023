#Se requiere desarrollar la arquitectura y diseño de un software para el manejo de un casino online, que sea accesible y cuente con medidas de seguridad para proteger el dinero de los usuarios, una plataforma de registro de usuarios, juegos en línea y acceso para configuración del sistema.
#Autores: Max Hernández Medrano, Jose David Jiménez Corrales, Luis Felipe Cabalceta Barrantes.
#05/06/2023. Última actualización: 20/08/2023

import getpass #Importamos la biblioteca getpass para la verificación de pines de seguridad.
import os #En caso de que alguien utilice una versión no actualizada de Python, se importa os para evitar presentar problemas de compatibilidad.
import random #Biblioteca random sobre la que de desarrollan los juegos del casino

usuariosRegistrados = [] #Creamos un arreglo en el que almacenaremos la información de los usuarios [[idUsuario],[pinUsuario]]
saldo = 0
moneda = "Dolares"
montoMinimo = 1500

#Definimos la función nuevoUsuario para llamar al bloque de código que compone la creación de un nuevo usuario.
def nuevoUsuario():
    global usuariosRegistrados #A través del keyword global accedemos al arreglo usuariosRegistrados desde la función.
    global saldo, moneda, montoMinimo
    print("Bienvenido al Módulo de Registro de Nuevo Usuario. Te solicitaremos tu ID, nombre y pin de seguridad para que podás acceder a nuestro casino")
    intentos = 3
    
    while intentos > 0: #Definimos un ciclo while en el que definimos que se detenga una vez sea igual a 0.
        idUsuario = input("Ingrese su ID de Usuario (Mínimo 5 caracteres alfanuméricos): \n") #Solicitamos al usuario el ID que desea registrar.
        if len(idUsuario) < 5: #Utilizamos estructuras de decisión para generar las condiciones del id del usuario.
            intentos -= 1
            print("El ID ingresado es demasiado corto. Intentos restantes: {}".format(intentos))
        elif idUsuario in [usuario[0] for usuario in usuariosRegistrados]: #Realizamos la validación del usuario ya registrado buscando en nuestro arreglo.
            intentos -= 1
            print("El ID {} ya está registrado. Intentos restantes: {}".format(idUsuario, intentos))
        else:
            break #Terminamos el ciclo.
        
    if intentos == 0:
        print("Se excedió el máximo de intentos para ingresar un ID válido, volviendo al menú principal")
        mostrarMenu()
    else:
        nombreUsuario = input("Ingrese un nombre para mostrarse:\n") #Solicitamos al usuario el nombre que desea que se le muestre en pantalla.
        
        while True: #Generamos otro ciclo while para solicitar el pin al usuario.
            pinUsuario = getpass.getpass("Ingrese su PIN de seguridad de 6 dígitos: ") #Importamos la biblioteca getpass para proteger la contraseña.
            if len(pinUsuario) != 6: #Validamos la longitud del pin con la funcion len() para que sea igual a 6 dígitos.
                print("El PIN ingresado no es válido")
            else:
                confirmacionPin = getpass.getpass("Ingrese nuevamente su PIN de seguridad: ") #Realizamos la confirmación del pin.
                if pinUsuario == confirmacionPin: 
                    print("PIN registrado con éxito.")
                    usuariosRegistrados.append((idUsuario, pinUsuario)) #Utilizando la funcion append() agregamos al arreglo ambos valores y lo convertimos en bidimensional, asignando para cada variable valores diferentes.
                    informacion = "Usuario {}, Pin {}".format(idUsuario, pinUsuario) #Almacenamos la información en un string.
                    try:
                        with open("usuariosPines.txt", "a") as file: #Abrimos el archivo usuariosPines donde almacenaremos la información del arreglo en un .txt
                            file.write(informacion + "\n") #Escribimos en el archivo.
                        print("Información almacenada con éxito") 
                    except Exception as e:
                        print("No se pudo guardar la información en el archivo:", e)
                        
                    realizarDeposito(saldo, moneda, montoMinimo)  # Llamar a realizarDeposito después de registrar el usuario
                    break
                        
def cargarTiposDeCambio():
    tiposDeCambio = {}
    with open("configuracionAvanzada.txt", "r") as file:
        for line in file:
            moneda, valor = line.strip().split(":")
            tiposDeCambio[moneda] = float(valor)
            print("Moneda:", moneda, "Valor:", valor)
    return tiposDeCambio


def realizarDeposito(saldo, moneda, montoMinimo):
    tiposDeCambio = cargarTiposDeCambio()

    print("DreamWorld Casino es un casino de alta gama. Para completar el registro, debe realizar un depósito mínimo de ${}.".format(montoMinimo))

    intentos = 3
    
    while intentos > 0:
        print("Intentos restantes:", intentos)
        monedaElegida = input("Ingrese el número de la moneda en la que desea realizar el depósito (1. Dólares, 2. Colones, 3. Bitcoin o 4. Euros): ")
        
        if monedaElegida == "1":
            monedaNombre = "Dolares"
            tipoCambio = 1.0  # Valor predeterminado para Dolares
        elif monedaElegida == "2":
            monedaNombre = "Colones"
            tipoCambio = tiposDeCambio["Colones"]
        elif monedaElegida == "3":
            monedaNombre = "Bitcoin"
            tipoCambio = tiposDeCambio["Bitcoin"]
        elif monedaElegida == "4":
            monedaNombre = "Euro"
            tipoCambio = tiposDeCambio["Euro"]
        else:
            print("Opción inválida.")
            continue  # Volver a solicitar la monedaElegida
        
        monto = float(input("Ingrese el monto que desea depositar: "))
        
        calculoMontoMinimo = montoMinimo / tipoCambio
        
        if monto >= calculoMontoMinimo:
            usuario = input("Ingrese su ID de usuario: ")
            if usuario in usuariosRegistrados:
                saldoTemporal = usuariosRegistrados[usuario]
            else:
                saldoTemporal = monto
            print("Depósito exitoso. Saldo actual: {} , {}".format(saldoTemporal, monedaNombre))
            mostrarMenu()
            break
        else:
            print("El depósito mínimo equivalente es {} {}.".format(calculoMontoMinimo, monedaNombre))

        intentos -= 1
    
    if intentos == 0:
        print("Se excedieron los intentos. Volviendo al menú principal.")
        

#Definimos las funciones dreamWorldCasino(), configuracionAvanzada() y salir() como funciones vacías por ahora, para evitar errores a la hora de llamarlas.
def cargarUsuarios():
    global usuariosRegistrados
    try:
        with open("usuariosPines.txt", "r") as file:
            for line in file.readlines():
                idUsuario, pinUsuario = line.strip().split(", ")
                usuariosRegistrados.append([idUsuario, pinUsuario])
        return usuariosRegistrados
    except FileNotFoundError:
        print("¡Archivo de usuarios no encontrado!")
        return []

def autenticarUsuario():
    global usuariosRegistrados  # Acceder a la variable global
    maxIntentos = 3
    while maxIntentos > 0:
        inputId = input("Ingrese su ID: ")
        inputPin = getpass.getpass("Ingrese su PIN: ")

        for usuario in usuariosRegistrados:  # Cambiar usuarios por usuariosRegistrados
            if usuario[0] == inputId and usuario[1] == inputPin:
                return usuario[0]

        maxIntentos -= 1
        if maxIntentos > 0:
            print("Credenciales inválidas. Le quedan {} intentos.".format(maxIntentos))
        else:
            print("Se excedió el máximo de intentos para ingresar su PIN.")
            return None


def dreamWorldCasino():
    if len(usuariosRegistrados) == 0:
        print("No hay usuarios registrados. Volviendo al menú principal.")
        mostrarMenu()
        return

    idUsuario = autenticarUsuario()

    if idUsuario is None:
        print("Se excedió el máximo de intentos para ingresar su ID o PIN, volviendo al menú principal")
        mostrarMenu()
        return

    print("Bienvenido, {}. ¿Qué querés hacer?".format(idUsuario))
    saldo = saldoTemporal

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


#MENÚ PRINCIPAL DEL PROGRAMA.
#Definimos mostrarMenu como la función principal para mostrar en pantalla el menú al usuario y las 4 secciones que componen el software. 
def mostrarMenu():
    print("Bienvenido a DreamWorld Casino. Elija la opción que desea:")
    print("1. Registro de usuario nuevo")
    print("2. DreamWorld Casino")
    print("3. Configuración Avanzada")
    print("4. Salir")

   
#Solicitamos al usuario que ingrese a través de un input la sección a la que desea ingresar.  
    opcion = input("Ingresa el número de opción: \n")

    if opcion == "1": #Definimos las condiciones a través de estructuras de decisión (if/elif/else). 
        nuevoUsuario()
    elif opcion == "2":
        dreamWorldCasino()
    elif opcion == "3":
        configuracionAvanzada()
    elif opcion == "4":
        print("Gracias por visitar DreamWorld Casino. Vuelva pronto")
        salir()
    else:
        print("Opción inválida. Por favor, selecciona una opción valida")
mostrarMenu()
        
