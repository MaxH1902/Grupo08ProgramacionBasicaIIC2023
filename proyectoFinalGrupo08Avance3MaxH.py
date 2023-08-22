#Se requiere desarrollar la arquitectura y diseño de un software para el manejo de un casino online, que sea accesible y cuente con medidas de seguridad para proteger el dinero de los usuarios, una plataforma de registro de usuarios, juegos en línea y acceso para configuración del sistema.
#Autores: Max Hernández Medrano, Jose David Jiménez Corrales, Luis Felipe Cabalceta Barrantes.
#05/06/2023. Última actualización: 20/08/2023

import getpass #Importamos la biblioteca getpass para la verificación de pines de seguridad.
import os #En caso de que alguien utilice una versión no actualizada de Python, se importa os para evitar presentar problemas de compatibilidad.
import random #Biblioteca random sobre la que de desarrollan los juegos del casino
import time #Importamos la biblioteca time para el juego de tragamonedas.

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
                    except Exception as e: #Buena práctica almacenar el manejo de errores en la variable e. 
                        print("No se pudo guardar la información en el archivo:", e)
                        
                    realizarDeposito(saldo, moneda, montoMinimo)  #Llamar a realizarDeposito después de registrar el usuario
                    break
                        
def cargarTiposDeCambio(): #Definimos la función que se va a encargar de cargas los tipos de cambio desde el archivo de configuración avanzada.
    tiposDeCambio = {} #Creamos un diccionario para almacenar los tipos de cambio.
    with open("configuracionAvanzada.txt", "r") as file: #Abrimos el archivo
        for line in file: #Utilizamos un ciclo en el que recorremos las líneas del diccionario.
            moneda, valor = line.strip().split(":") #Dividimos la información almacenada dentro de la lista utilizando : como separador para sustraer la información.Con strip eliminamos los espacios entre cada uno de los valores.
            tiposDeCambio[moneda] = float(valor)
            print("Moneda:", moneda, "Valor:", valor)
    return tiposDeCambio #Utilizamos la keyword return para devolver el valor de los tipos de cambio.


def realizarDeposito(saldo, moneda, montoMinimo): #Definimos la funcion para realizar el depósito inicial.
    tiposDeCambio = cargarTiposDeCambio()

    print("DreamWorld Casino es un casino de alta gama. Para completar el registro, debe realizar un depósito mínimo de ${}.".format(montoMinimo))

    intentos = 3
    
    while intentos > 0: #Creamos un ciclo while para definir la cantidad de intentos.
        print("Intentos restantes:", intentos)
        monedaElegida = input("Ingrese el número de la moneda en la que desea realizar el depósito (1. Dólares, 2. Colones, 3. Bitcoin o 4. Euros): ")
        
        if monedaElegida == "1": #Utilizamos estructuras de decisión para crear las condiciones del tipo de cambio elegido a la hora de realizar el depósito.
            monedaNombre = "Dolares"
            tipoCambio = 1.0
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
            continue 
        
        monto = float(input("Ingrese el monto que desea depositar: "))
        
        calculoMontoMinimo = montoMinimo / tipoCambio #Realizamos la conversión para calcular el monto mínimo en las diferentes monedas.
        
        if monto >= calculoMontoMinimo:
            usuario = input("Ingrese su ID de usuario: ")
            if usuario in usuariosRegistrados:
                saldoTemporal = usuariosRegistrados[usuario]
            else:
                saldoTemporal = monto
            print("Depósito exitoso. Saldo actual: {} , {}".format(saldoTemporal, monedaNombre)) #Notificamos que el deposito fue exitoso y mostramos el saldo en la moneda elegida.
            mostrarMenu()
            break
        else:
            print("El depósito mínimo equivalente es {} {}.".format(calculoMontoMinimo, monedaNombre))

        intentos -= 1
    
    if intentos == 0:
        print("Se excedieron los intentos. Volviendo al menú principal.")
        

#Definimos las funciones para el módulo de dreamWorldCasino()
def cargarUsuarios(): #Cargamos los usuarios desde el archivo de texto previamente creado. 
    global usuariosRegistrados #Accedemos al arreglo usuariosRegistrados.
    try:
        with open("usuariosPines.txt", "r") as file: #Abrimos nuestro archivo para leer y buscar la validación de los usuarios y el pin.
            for line in file.readlines():
                idUsuario, pinUsuario = line.strip().split(", ")
                usuariosRegistrados.append([idUsuario, pinUsuario]) 
        return usuariosRegistrados
    except FileNotFoundError: #A través de try y except definimos el manejo de errores si no existiese un usuario previamente creado.
        print("¡Archivo de usuarios no encontrado!")
        return [] #Devolvemos una lista vacía en caso de que el usuario no sea encontrado.

def autenticarUsuario(): #Creamos la función que se encarga de realizar la autenticación del usuario.
    global usuariosRegistrados
    maxIntentos = 3
    while maxIntentos > 0:
        inputId = input("Ingrese su ID: ") #Volvemos a solicitar el id del usuario y lo almacenamos en la variable inputId
        inputPin = getpass.getpass("Ingrese su PIN: ") #Volvemos a solicitar el pin del usuario y lo almacenamos en la variable inputPin

        for usuario in usuariosRegistrados: #Con un ciclo for realizamos la validación buscando en nuestro arreglo usuariosRegistrados.
            if usuario[0] == inputId and usuario[1] == inputPin: #Creamos las estructuras de decisión para nuestra validación.
                return usuario[0] #Devolvemos el primer usuario encontrado con las condiciones establecidas.

        maxIntentos -= 1
        if maxIntentos > 0:
            print("Credenciales inválidas. Le quedan {} intentos.".format(maxIntentos))
        else:
            print("Se excedió el máximo de intentos para ingresar su PIN.")
            return None #Similar al caso anterior retornamos un valor para definir su ausencia.

def dreamWorldCasino(): #Definimos la función principal del módulo del casino comenzando con la validación.
    if len(usuariosRegistrados) == 0:
        print("No hay usuarios registrados. Volviendo al menú principal.")
        mostrarMenu()
        return

    idUsuario = autenticarUsuario() #Llamamos a la función autenticarUsuario para realizar la validación.

    if idUsuario is None: #Si el espacio está vacío notificamos error.
        print("Se excedió el máximo de intentos para ingresar su ID o PIN, volviendo al menú principal")
        mostrarMenu()
        return

    print("Bienvenido, {}. ¿Qué querés hacer?".format(idUsuario)) #Definimos el menú del módulo a través de un ciclo while y estructuras de decisión.

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

def retirarDinero(idUsuario):
    print("Función no definida")

def depositarDinero(idUsuario):
    print("Función no definida")

def verSaldo(idUsuario):
    print("Funcion no definida")
        
def juegosEnLinea(idUsuario): #Creamos la función que contendrá ambos juegos, definiendo el menú con un ciclo while.
    while True:
        print("Juegos en línea")
        print("1. Blackjack")
        print("2. Tragamonedas")
        print("3. Volver al menú principal")
        opcion = input("Ingrese el número de opción: ")
        if opcion == "1":
            blackjack()
            mostrarInstrucciones()
        elif opcion == "2":
            tragamonedas()
            mostrarInstrucciones()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

def mostrarInstrucciones(): #Aquí deberíamos mostrar las instrucciones de ambos juegos.
    print("Instrucciones para el juego de Blackjack:")
    print("Instrucciones para el juego de Tragamonedas:")

def blackjack(): #Definimos la función de nuestro juego de BlackJack.
    print("Bienvenido al juego de Blackjack")
        
    def obtenerCarta(carta): #Definimos la primera función para obtener las cartas validando A como si fuera un 11 y J, Q y K como 10.
        if carta == "A":
            return 11
        elif carta in ["J", "Q", "K"]:
            return 10
        else:
            return int(carta) #Devolvemos el valor en un formato entero.
    
    def obtenerValor(mano): #Definimos la función para obtener el valor de ambas cartas.
        valor = sum([obtenerCarta(carta) for carta in mano]) #Sumamos los valores.
        ases = mano.count("A") #Contamos los ases en la mano.
        while valor > 21 and ases: #Si el valor es mayor a 21 y hay as en la mano, le resta 10 al as como en el juego real.
            valor -= 10
            ases -= 1
        return valor #Retornamos el valor final de ambas cartas sumadas.
    
    def mostrarMano(mano, ocultarPrimeraCarta=False): #Definimos la función para ocultar la primera carta, si es falso
        if ocultarPrimeraCarta:
            print(f"Mano: {mano[1:]}")#Utilizamos el slicing para mostrar los valores exceptuando el primero.
        else:
            print(f"Mano: {mano}")
    
    def jugarBlackjack(): 
        mazo = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
        random.shuffle(mazo)
        manoJugador = [mazo.pop(), mazo.pop()]  #Repartimos las dos primeras cartas al jugador. A través de del método pop podemos simular que tomamos el último valor de la lista mazo.
        manoCrupier = [mazo.pop(), mazo.pop()]  #Repartimos las dos primeras cartas al crupier
        
        mostrarMano(manoJugador)
        print(f"Carta visible del crupier: {manoCrupier[0]}")  #Mostramos solo la primera carta del crupier
        
        while obtenerValor(manoJugador) < 21: #Utilizamos un ciclo while para obtener el valor y con condiciones definimos si desea solicitar o no otra carta.
            otraCarta = input("¿Quieres pedir una carta (P) o parar (S)? ").upper() #A través de upper nos permite evitar errores de transcripción.
            if otraCarta == "P":
                nuevaCarta = mazo.pop() #Tomamos nuevamente el último elemento del mazo.
                manoJugador.append(nuevaCarta) #Agregamos el valor de nuevaCarta al final de la lista manoJugador, lo que simula que el jugador recibe una nueva carta y la coloca en su mano.
                mostrarMano(manoJugador)
            else:
                break
        
        while obtenerValor(manoCrupier) < 17: #El ciclo while se ejecuta mientras el valor de la mano del crupier sea menor que 17. En las reglas reales el crupier está obligado a pedir carta hasta sumar al menos 17.
            nuevaCarta = mazo.pop()
            manoCrupier.append(nuevaCarta)
        
        mostrarMano(manoCrupier, ocultarPrimeraCarta=True)  # Mostrar todas las cartas del crupier
        
        #Mostramos valores de ambos jugadores.
        valorJugador = obtenerValor(manoJugador)
        valorCrupier = obtenerValor(manoCrupier)
        
        if valorJugador > 21: #Si las cartas del usuario suman más de 21 ha perdido.
            print("Has perdido.")
        elif valorCrupier > 21 or valorJugador > valorCrupier: #Si es menor que 21 pero mayor que el grupier ha ganado.
            print("¡Has ganado!")
        elif valorJugador == valorCrupier: #En caso de empate la casa siempre gana.
            print("Empate. Casa gana")
        else:
            print("El crupier gana.")
    
    #Llamamos para comenzar el juego
    jugarBlackjack()


def tragamonedas(): #Definimos el módulo de tragamonedas.
    print("Bienvenido al juego de Tragamonedas")
        
    def jugarTragamonedas(): #Definimos las figuras que componen nuestra máquina.
        figuras = ["@", "#", "+", "7"]
        acumulado = 1000 #Definimos la variable del acumulado.
        contadorJugadas = 0
        
        while True:
            input("Presione Enter para jalar la palanca e iniciar el juego") #Imprimimos información para notificar al usuario que el juego inicia con enter.
            resultado = [random.choice(figuras) for _ in range(3)]  #Seleccionamos aleatoriamente un elemento de la lista figuras. La función random.choice() toma una secuencia generada al azar.
            
            print("Este es el resultado:")
            for figura in resultado: 
                print(figura, end=" ") #Imprimimos el resultado con un espacio entre cada uno de los elementos.
                time.sleep(1.5) #Creamos una pausa entre la impresión de cada elemento de 1.5 segundos.
            print()
            
            contadorJugadas += 1
            if contadorJugadas % 20 == 0:
                print("¡Ganaste el acumulado!")
                acumulado = 0
            elif contadorJugadas % 15 == 0:
                print("Ganaste el triple de tu dinero.")
                acumulado += acumulado
            elif contadorJugadas % 10 == 0:
                print("Ganaste el doble de tu dinero.")
                acumulado += acumulado
            elif contadorJugadas % 5 == 0:
                print("Ganaste, recuperas tu dinero.")
                acumulado += acumulado
            
            print(f"Acumulado: {acumulado}")
            
            jugarNuevamente = input("¿Quieres jugar nuevamente? (s/n): ")
            if jugarNuevamente.lower() != "s":
                break
    
    jugarTragamonedas()

def delete_user():
    print("Eliminar Usuario")



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
        
