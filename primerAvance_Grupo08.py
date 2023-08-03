  #Se requiere desarrollar la arquitectura y diseño de un software para el manejo de un casino online, que sea accesible y cuente con medidas de seguridad para proteger el dinero de los usuarios, una plataforma de registro de usuarios, juegos en línea y acceso para configuración del sistema.
#Autor: Max Hernández Medrano
#05/06/2023

#Importamos la biblioteca getpass para la verificación de PIN.
import getpass

#Definimos la variable global usuarios_registrados para almacenar la lista de usuarios registrados durante toda la ejecución del programa.
usuarios_registrados = []

#Utilizamos la función def() para definir mostrar_menu como la función para mostrar en pantalla el menú al usuario y las 4 secciones que componen el software. 
def mostrar_menu():
    print("Bienvenido a DreamWorld Casino. Por favor, elegí una opción:")
    print("1. Registro de usuario nuevo")
    print("2. DreamWorld Casino")
    print("3. Configuración Avanzada")
    print("4. Salir")
    
#Solicitamos al usuario que ingrese a través de un input la sección a la que desea ingresar. Definimos las condiciones a través de estructuras de decisión (if/elif/else).  
    opcion = input("Ingresa el número de opción: \n")

    if opcion == "1":
        nuevo_usuario()
    elif opcion == "2":
       # Importamos el módulo Modulo_DreamWorld_Casino y llamamos a la función dreamworld_casino().
        import Modulo_DreamWorld_Casino
        Modulo_DreamWorld_Casino.dreamworld_casino()
    elif opcion == "3":
        configuracion_avanzada()
    elif opcion == "4":
        salir()
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

#Definimos la función nuevo_usuario para llamar al bloque de código que compone la creación de un nuevo usuario.
#Generamos un ciclo while para verificar la cantidad de intentos del usuario para elegir su id y definimos la constante intentos = 3.
#Utilizamos la función len para extraer la cantidad de carácteres requeridos y que cumpla con los requerimientos del sistema.
#A través de estructuras de decisión definimos las condiciones de verificación para continuar con el siguiente paso, elección del PIN de seguridad.      
def nuevo_usuario():
    print("Registro de Nuevo Usuario")
    intentos = 3
    usuarios_registrados = []
    while intentos > 0:
        id_usuario = input("Ingrese su ID de Usuario (Mínimo 5 caracteres alfanuméricos): \n")
        if len(id_usuario) < 5:
            intentos -= 1
            print("El ID ingresado es demasiado corto. Intentos restantes: {}".format(intentos))
        elif id_usuario in usuarios_registrados:
            intentos -= 1
            print("El ID {} ya está registrado. Intentos restantes: {}".format(id_usuario, intentos))
        else:
            break
#Definimos que cuando el contador de intentos llega a 0, se regresa al menú principal.       
    if intentos == 0:
            print("Se excedió el máximo de intentos para ingresar un ID válido, volviendo al menú principal")
            mostrar_menu()
#Realizamos la elección del PIN de seguridad. Definimos la condición de caracteres a través de if. Nuevamente utilizamos la función len para extraer la cantidad de objetos que requerimos.
#Llamamos a la biblioteca getpass. Realizamos la verificación del pin a través de if para mostrar mensaje a usuario de PIN Registrado correctamente.
    else:
        # Solicitsmos al usuario que ingrese un nombre para mostarse.
        nombre_usuario = input("Ingrese un nombre,para mostarse")
        while True:
            pin = getpass.getpass("Ingrese su PIN de seguridad de 6 dígitos")
            if len(pin) != 6:
                print("El pin ingresado no es válido")
            else:
                confirmacion_pin = getpass.getpass("Ingrese nuevamente su PIN de seguridad: ")
                if pin == confirmacion_pin:
                    print("PIN registrado con éxito.")
                    #Agregamos el ID y el nombre del usuario a la lista global usuarios_registrados.
                    usuarios_registrados.append((id_usuario, nombre_usuario))
                    #llamamos a la funcion deposito_minimo() para solicitar al usuario que realice un deposito minimo
                    deposito_minimo()
                    
                    break
                else:
                    print("El PIN de confirmación no coincide. Por favor, ingrese nuevamente el PIN.")

def deposito_minimo():
    #definimos el monto del deposito minimo, en este caso sera de $1500
    monto_minimo = 1500
    #definimos los tipo de cambio
    tipo_cambio_colones = 600
    tipo_cambio_bitcoin = 50000
    intentos = 3
    while intentos > 0:
        print("DreamWorld Casino es un casino de alta gama. Para completar el registro, debe realizar un depósito mínimo de ${}.".format(monto_minimo))
        print("Puede realizar el depósito en dólares, colones o bitcoin.")
        moneda = input("Ingrese la moneda en la que desea realizar el depósito (dólares, colones o bitcoin): ")
        monto = float(input("Ingrese el monto que desea depositar: "))
        if moneda == "colones":
            monto /= tipo_cambio_colones
        elif moneda == "bitcoin":
            monto *= tipo_cambio_bitcoin
        if monto >= monto_minimo:
            print("Depósito realizado con éxito. Su cuenta ahora tiene un saldo de ${}.".format(monto))
            #Llamamos a la función mostrar_menu() para volver a mostrar el menú después de realizar el depósito con éxito.
            mostrar_menu()
            break
        else:
            intentos -= 1
            print("El monto depositado no alcanza el mínimo requerido. Intentos restantes: {}".format(intentos))
    if intentos == 0:
        print("Se excedió el máximo de intentos para depositar el mínimo de dinero requerido, volviendo al menú principal")
        mostrar_menu()
        
    
    
#Definimos las funciones dreamworld_casino(), configuracion_avanzada() y salir() como funciones vacías por ahora, para evitar errores a la hora de llamarlarla 
def dreamworld_casino():
    print("Esta sección está en desarrollo.")
    mostrar_menu()

def configuracion_avanzada():
    print("Esta sección está en desarrollo.")
    mostrar_menu()


def salir():
    print("Gracias por utilizar DreamWorld Casino. ¡Hasta pronto!")
    
                  


#Falta integrar la verificación se usuarios almacenados de la parte del registro de nuevo usuario.(*Listas)
#Falta desarrollar el ciclo que regresa al menú de inicio.
#Falta desarrollar sección de "Depósito Mínimo". (*Base de datos con tipos de cambio, biblioteca os, estructuras del sistema de archivos).

mostrar_menu()
