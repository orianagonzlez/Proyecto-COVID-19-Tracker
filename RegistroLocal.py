from colorama import init, Fore, Style
from Funciones import pedir_entero_positivo_validado

init(autoreset=True)

class Persona:
    '''
    Clase de personas. Es necesario indicar: nombre completo y edad.
    '''
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class NoInfectado(Persona):
    def __init__(self, nombre, edad, telefono):
        Persona.__init__(self, nombre, edad)
        self.telefono = telefono

    def __str__(self):
        return "\t• Estado: No infectado \n\t• Nombre completo: {} \n\t• Edad: {} \n\t• Telefono: {}".format(self.nombre, self.edad, self.telefono)

    def to_string(self):
        return "No infectado" + "," + self.nombre + "," + str(self.edad) + "," + str(self.telefono) + ",X,X,X,X"

class EnRevision(NoInfectado):
    def __init__(self, nombre, edad, telefono):
        NoInfectado.__init__(self, nombre, edad, telefono)
    
    def __str__(self):
        return "\t• Estado: En revision \n\t• Nombre completo: {} \n\t• Edad: {} \n\t• Telefono: {}".format(self.nombre, self.edad, self.telefono)

    def to_string(self):
        return "En revision" + "," + self.nombre + "," + str(self.edad) + "," + str(self.telefono) + ",X,X,X,X"

class PosibleInfectado(Persona):
    def __init__(self, nombre, edad, direccion, ciudad, estado):
        Persona.__init__(self, nombre, edad)
        self.direccion = direccion
        self.ciudad = ciudad
        self.estado = estado

    def __str__(self):
        return "\t• Estado: Posible infectado \n\t• Nombre completo: {} \n\t• Edad: {} \n\t• Datos de cuarentena: \n\t  - Direccion: {} \n\t  - Ciudad: {} \n\t  - Estado: {}".format(self.nombre, self.edad, self.direccion, self.ciudad, self.estado)

    def to_string(self):
        return "Posible infectado" + "," + self.nombre + "," + str(self.edad) + ",X"  + "," + self.direccion + "," + self.ciudad + "," + self.estado + ",X"

class Infectado(PosibleInfectado):
    def __init__(self, nombre, edad, direccion, ciudad, estado, medico):
        PosibleInfectado.__init__(self, nombre, edad, direccion, ciudad, estado)
        self.medico = medico

    def __str__(self):
        return "\t• Estado: Infectado \n\t• Nombre completo: {} \n\t• Edad: {} \n\t• Datos de cuarentena: \n\t  - Direccion: {} \n\t  - Ciudad: {} \n\t  - Estado: {} \n\t• Medico: {}".format(self.nombre, self.edad, self.direccion, self.ciudad, self.estado, self.medico)

    def to_string(self):
        return "Infectado" + "," + self.nombre + "," + str(self.edad) + ",X"  + "," + self.direccion + "," + self.ciudad + "," + self.estado + "," + self.medico

def validar_nombre(nombre):
    '''
    Función para validar que el argumento este conformado únicamente de letras y espacios.

    Si lo anterior se cumple retorna verdadero, de lo contrario retorna falso.
    '''
    nombre = nombre.replace(" ", "")
    return nombre.isalpha()

def verificar_nombre(nombre):
    '''
    Función que recibe como argumento el nombre completo y verifica si este ya se encuentra en la base de datos del registro local.

    Si el usuario ya esta registrado retorna verdadero, si no retorna falso.
    '''
    try:
        with open("BaseDeDatosRegistroLocal.txt", "r") as archivo_usuarios:
            all_users = archivo_usuarios.readlines()
        for usuario in all_users:
            user = usuario[:-1].split(",")
            if user[1] == nombre:
                return True
        return False
    except:
        print("\nTodavía no hay ningún usuario registrado. Ingrese los datos pedidos a continuación para registrarse. \n")

def buscar(nombre):
    '''
    Función para buscar el nombre completo pasado como argumento en la base de datos del registro local.
    
    Si encuentra al usuario, retorna al usuario como un objeto.
    '''
    with open("BaseDeDatosRegistroLocal.txt", "r") as archivo_usuarios:
        all_users = archivo_usuarios.readlines()
    for usuario in all_users:
        user = usuario[:-1].split(",")
        if user[1] == nombre:
            if user[0] == "No infectado":
                return NoInfectado(user[1], user[2], user[3])
            elif user[0] == "En revision":
                return NoInfectado(user[1], user[2], user[3])
            elif user[0] == "Posible infectado":
                return PosibleInfectado(user[1], user[2], user[4], user[5], user[6])
            else:
                print(user[0])
                return Infectado(user[1], user[2], user[4], user[5], user[6], user[7])

def preguntar_sintoma(pregunta):
    respuesta = pedir_entero_positivo_validado("\n" + Fore.MAGENTA + pregunta + "\n\nSi la respuesta es afirmativa ingrese 1, si la respuesta es negativa ingrese 0: ")
    while respuesta != 0 and respuesta != 1:
        respuesta = pedir_entero_positivo_validado(pregunta + "\n\nSi la respuesta es afirmativa ingrese 1, si la respuesta es negativa ingrese 0: ")
    return respuesta

def ver():
    '''
    Funcion para ver los usuarios en la base de datos del registro local
    '''
    print("Estos son los usuarios registrados actualmente:\n")
    usuarios = []
    with open("BaseDeDatosRegistroLocal.txt", "r") as archivo_usuarios:
        all_users = archivo_usuarios.readlines()
        for usuario in all_users:
            user = usuario[:-1].split(",")
            if user[0] == "No infectado":
                usuarios.append(NoInfectado(user[1], user[2], user[3]))
            elif user[0] == "En revision":
                usuarios.append(NoInfectado(user[1], user[2], user[3]))
            elif user[0] == "Posible infectado":
                usuarios.append(PosibleInfectado(user[1], user[2], user[4], user[5], user[6]))
            else:
                usuarios.append(Infectado(user[1], user[2], user[4], user[5], user[6], user[7]))
        
    usuarios.sort(key= lambda usuario: usuario.nombre)
    for i, user in enumerate(usuarios, 1):
        print(Fore.CYAN + str(i) + '.')
        print(user)

def registrar():
    print("Por favor, ingrese los siguientes datos.\n")

    nombre = input("Ingrese su nombre completo: ")  #validar que no este en el txt
    while not validar_nombre(nombre):
        nombre = input("Ingrese su nombre completo. Solo puede contener letras y espacios: ")

    if verificar_nombre(nombre):
        print("Usted ya esta registrado. A continuacion se muestran sus datos:")
        return buscar(nombre)
    else:

        edad = pedir_entero_positivo_validado("Ingrese su edad: ")
        while edad > 100 or edad < 5:
            edad = pedir_entero_positivo_validado("Ingrese su edad. Debe estar comprendida entre 5 y 100 años: ")
        
        preguntas = ["¿Tiene secreciones nasales?", "¿Tiene dolor de garganta?", "¿Tiene tos?",
                    "¿Tiene fiebre?", "¿Tiene dificultad para respirar?"]
        sintomas = 0

        for sintoma in preguntas:
            if preguntar_sintoma(sintoma):
                sintomas += 1
        
        print("")
        if sintomas == 0:
            print("Usted no esta infectado.\n")
            numero = pedir_entero_positivo_validado("Ingrese su numero de telefono: ")

            usuario = NoInfectado(nombre.title(), edad, numero)
        elif sintomas < 3:
            print("Usted estara en revision.\n")
            numero = pedir_entero_positivo_validado("Ingrese su numero de telefono: ")

            usuario = EnRevision(nombre.title(), edad, numero)
        elif sintomas < 5:
            print("Usted es un posible infectado. Debe realizar cuarentena.\n")
            direccion = input("Ingrese la direccion donde realizara cuarentena: ")
            ciudad = input("Ingrese la ciudad donde realizara cuarentena: ")
            estado = input("Ingrese el estado donde realizara cuarentena: ")

            usuario = PosibleInfectado(nombre.title(), edad, direccion, ciudad.title(), estado.title())
        else:
            print("Usted esta infectado. Debe realizar cuarentena y consultar con un medico.\n")
            direccion = input("Ingrese la direccion donde realizara cuarentena: ")
            ciudad = input("Ingrese la ciudad donde realizara cuarentena: ")
            estado = input("Ingrese el estado donde realizara cuarentena: ")
            medico = input("Ingrese el nombre de su medico tratante: ")
            while not validar_nombre(medico):
                medico = input("Ingrese el nombre de su medico tratante. Solo puede contener letras y espacios: ")

            usuario = Infectado(nombre.title(), edad, direccion, ciudad.title(), estado.title(), medico.title())

        #En caso de que el archivo de texto no exista, se crea
        with open("BaseDeDatosRegistroLocal.txt", "a+") as archivo_usuarios:
            archivo_usuarios.write(usuario.to_string() + "\n")

        print("\nEl usuario '{}' se ha registrado correctamente.\n".format(usuario.nombre))
        return usuario
