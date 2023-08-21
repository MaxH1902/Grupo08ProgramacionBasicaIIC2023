#Se requiere desarrollar la arquitectura y diseño de un software para el manejo de un casino online, que sea accesible y cuente con medidas de seguridad para proteger el dinero de los usuarios, una plataforma de registro de usuarios, juegos en línea y acceso para configuración del sistema.
#Autor: Max Hernández Medrano
#05/06/2023

#Importamos la biblioteca getpass para la verificación de PIN.
import getpass

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
        dreamworld_casino()
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
#Realizamos la elección del PIN de seguridad. Definimos la condición de caracteres a través de if. Nuevamente utilizamos la función len para extraer la cantidad de objetos que requerimos.
#Llamamos a la biblioteca getpass. Realizamos la verificación del pin a través de if para mostrar mensaje a usuario de PIN Registrado correctamente.
    else:
        while True:
            pin = getpass.getpass("Ingrese su PIN de seguridad de 6 dígitos")
            if len(pin) != 6:
                print("El pin ingresado no es válido")
            else:
                confirmacion_pin = getpass.getpass("Ingrese nuevamente su PIN de seguridad: ")
                if pin == confirmacion_pin:
                    print("PIN registrado con éxito.")
                    break
                else:
                    print("El PIN de confirmación no coincide. Por favor, ingrese nuevamente el PIN.")
#Falta integrar la verificación se usuarios almacenados de la parte del registro de nuevo usuario.(*Listas)
#Faltaa desarrollar sección de "Depósito Mínimo". (*Base de datos con tipos de cambio, biblioteca os, estructuras del sistema de archivos).

mostrar_menu()
