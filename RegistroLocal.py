from colorama import init, Fore, Style
from Funciones import pedir_entero_positivo_validado

init(autoreset=True)

class Persona:
    '''
    Clase de personas. Sus atributos son nombre completo y edad.
    '''
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class NoInfectado(Persona):
    '''
    Clase hija de Persona. Corresponde a las personas no infectadas. Sus atributos son nombre completo, edad y número de teléfono.
    '''
    def __init__(self, nombre, edad, telefono):
        Persona.__init__(self, nombre, edad)
        self.telefono = telefono

    def __str__(self):
        return "\t• Estado: No infectado \n\t• Nombre completo: {} \n\t• Edad: {} \n\t• Telefono: {}".format(self.nombre, self.edad, self.telefono)

    def to_string(self):
        '''
        Función que retorna los datos de la persona en el formato para guardarlos en la base de datos del registro local.
        '''
        return "No infectado" + "," + self.nombre + "," + str(self.edad) + "," + str(self.telefono) + ",X,X,X,X"

class EnRevision(NoInfectado):
    '''
    Clase hija de NoInfectado. Corresponde a las personas que están en revisión. Sus atributos son nombre completo, edad y número de teléfono.
    '''
    def __init__(self, nombre, edad, telefono):
        NoInfectado.__init__(self, nombre, edad, telefono)
    
    def __str__(self):
        return "\t• Estado: En revision \n\t• Nombre completo: {} \n\t• Edad: {} \n\t• Telefono: {}".format(self.nombre, self.edad, self.telefono)

    def to_string(self):
        '''
        Función que retorna los datos de la persona en el formato para guardarlos en la base de datos del registro local.
        '''
        return "En revision" + "," + self.nombre + "," + str(self.edad) + "," + str(self.telefono) + ",X,X,X,X"

class PosibleInfectado(Persona):
    '''
    Clase hija de Persona. Corresponde a las personas que pueden estar infectadas. Sus atributos son nombre completo, edad, número de teléfono
    y dirección, ciudad y estado donde se realizará la cuarentena.
    '''
    def __init__(self, nombre, edad, direccion, ciudad, estado):
        Persona.__init__(self, nombre, edad)
        self.direccion = direccion
        self.ciudad = ciudad
        self.estado = estado

    def __str__(self):
        return "\t• Estado: Posible infectado \n\t• Nombre completo: {} \n\t• Edad: {} \n\t• Datos de cuarentena: \n\t   - Direccion: {} \n\t   - Ciudad: {} \n\t   - Estado: {}".format(self.nombre, self.edad, self.direccion, self.ciudad, self.estado)

    def to_string(self):
        '''
        Función que retorna los datos de la persona en el formato para guardarlos en la base de datos del registro local.
        '''
        return "Posible infectado" + "," + self.nombre + "," + str(self.edad) + ",X"  + "," + self.direccion + "," + self.ciudad + "," + self.estado + ",X"

class Infectado(PosibleInfectado):
    '''
    Clase hija de PosibleInfectado. Corresponde a las personas que están infectadas.Sus atributos son nombre completo, edad, número de teléfono,
    dirección, ciudad y estado donde se realizará la cuarentena y médico tratante.
    '''
    def __init__(self, nombre, edad, direccion, ciudad, estado, medico):
        PosibleInfectado.__init__(self, nombre, edad, direccion, ciudad, estado)
        self.medico = medico

    def __str__(self):
        return "\t• Estado: Infectado \n\t• Nombre completo: {} \n\t• Edad: {} \n\t• Datos de cuarentena: \n\t   - Direccion: {} \n\t   - Ciudad: {} \n\t   - Estado: {} \n\t• Medico: {}".format(self.nombre, self.edad, self.direccion, self.ciudad, self.estado, self.medico)

    def to_string(self):
        '''
        Función que retorna los datos de la persona en el formato para guardarlos en la base de datos del registro local.
        '''
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
        return False

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
                return EnRevision(user[1], user[2], user[3])
            elif user[0] == "Posible infectado":
                return PosibleInfectado(user[1], user[2], user[4], user[5], user[6])
            else:
                return Infectado(user[1], user[2], user[4], user[5], user[6], user[7])

def preguntar_sintoma(pregunta):
    '''
    Función que recibe como argumento una pregunta y le pregunta al usuario su respuesta.

    Si la respuesta es afirmativa(si) retorna 1 (que se traduce como verdadero), si es negativa (no) retorna 0 (que se traduce como falso).
    '''
    print(Fore.CYAN + "\n" + pregunta)
    respuesta = pedir_entero_positivo_validado("\n\tSi la respuesta es afirmativa (SI) ingrese 1, si la respuesta es negativa (NO) ingrese 0: ")
    while respuesta != 0 and respuesta != 1:
        respuesta = pedir_entero_positivo_validado("\n\tSi la respuesta es afirmativa (SI) ingrese 1, si la respuesta es negativa (NO) ingrese 0: ")
    return respuesta

def ver():
    '''
    Función que imprime todos los usuarios en la base de datos del registro local ordenados alfabéticamente según el nombre completo.
    '''
    print(Fore.MAGENTA + "Estos son los usuarios registrados actualmente:\n")
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
        print(user, end="\n\n")

def registrar():
    '''
    Función que en caso de que un usuario no esté registrado, lo clasifica entre no infectado, en revisión, posible infectado e 
    infectado según el número de síntomas que presente y lo registra en la base de datos del registro local. 

    Retorna al usuario como objeto.
    '''
    print(Fore.MAGENTA + "Por favor, ingrese los siguientes datos.\n")

    nombre = input("Ingrese su nombre completo: ").title()  
    while not validar_nombre(nombre):
        nombre = input("Ingrese su nombre completo. Solo puede contener letras y espacios: ").title()

    #Si el usuario no esta en la base de datos, se le realizan las preguntas y se le piden los datos necesarios
    if verificar_nombre(nombre):
        print("\nUsted ya está registrado. A continuación se muestran sus datos:\n")
        return buscar(nombre)
    else:

        edad = pedir_entero_positivo_validado("Ingrese su edad: ")
        while edad > 130:
            edad = pedir_entero_positivo_validado("Ingrese su edad. Debe estar comprendida entre 0 y 130 años: ")
        
        preguntas = ["¿Tiene secreciones nasales?", "¿Tiene dolor de garganta?", "¿Tiene tos?",
                    "¿Tiene fiebre?", "¿Tiene dificultad para respirar?"]
        sintomas = 0

        for sintoma in preguntas:
            if preguntar_sintoma(sintoma):
                sintomas += 1
        
        #De acuerdo a cuantos sintomas presente el usuario, se le clasifica en las 4 categorias y se le piden los datos correspondientes
        print("")
        if sintomas == 0:
            print(Fore.MAGENTA + "Usted no esta infectado.\n")
            numero = pedir_entero_positivo_validado("Ingrese su número de teléfono (Ej: 4142369321).\nDebe tener 10 dígitos, la cuenta empieza desde el primer dígito distinto de 0: ")
            while len(str(numero)) != 10:
                numero = pedir_entero_positivo_validado("Ingrese su número de teléfono (Ej: 4142369321).\nDebe tener 10 dígitos, la cuenta empieza desde el primer dígito distinto de 0: ")

            usuario = NoInfectado(nombre, edad, numero)
        elif sintomas < 3:
            print(Fore.MAGENTA + "Usted estará en revisión.\n")
            numero = pedir_entero_positivo_validado("Ingrese su número de teléfono (Ej: 4142369321).\nDebe tener 10 dígitos, la cuenta empieza desde el primer dígito distinto de 0: ")
            while len(str(numero)) != 10:
                numero = pedir_entero_positivo_validado("Ingrese su número de teléfono (Ej: 4142369321).\nDebe tener 10 dígitos, la cuenta empieza desde el primer dígito distinto de 0: ")

            usuario = EnRevision(nombre, edad, numero)
        elif sintomas < 5:
            print(Fore.MAGENTA + "Usted es un posible infectado. Debe realizar cuarentena.\n")
            direccion = input("Ingrese la dirección donde realizará cuarentena: ")
            ciudad = input("Ingrese la ciudad donde realizará cuarentena: ").title()
            while not validar_nombre(ciudad):
                ciudad = input("Ingrese la ciudad donde realizará cuarentena. Solo puede contener letras y espacios: ").title()

            estado = input("Ingrese el estado donde realizará cuarentena: ").title()
            while not validar_nombre(estado):
                estado = input("Ingrese el estado donde realizará cuarentena. Solo puede contener letras y espacios: ").title()

            usuario = PosibleInfectado(nombre, edad, direccion, ciudad, estado)
        else:
            print(Fore.MAGENTA + "Usted esta infectado. Debe realizar cuarentena y consultar con un medico.\n")
            direccion = input("Ingrese la dirección donde realizará cuarentena: ")
            ciudad = input("Ingrese la ciudad donde realizará cuarentena: ").title()
            while not validar_nombre(ciudad):
                ciudad = input("Ingrese la ciudad donde realizará cuarentena. Solo puede contener letras y espacios: ").title()

            estado = input("Ingrese el estado donde realizará cuarentena: ").title()
            while not validar_nombre(estado):
                estado = input("Ingrese el estado donde realizará cuarentena. Solo puede contener letras y espacios: ").title()

            medico = input("Ingrese el nombre de su médico tratante: ").title()
            while not validar_nombre(medico):
                medico = input("Ingrese el nombre de su médico tratante. Solo puede contener letras y espacios: ").title()

            usuario = Infectado(nombre, edad, direccion, ciudad, estado, medico)

        #En caso de que el archivo de texto no exista, se crea
        with open("BaseDeDatosRegistroLocal.txt", "a+") as archivo_usuarios:
            archivo_usuarios.write(usuario.to_string() + "\n")

        print("\nEl usuario '{}' se ha registrado correctamente.\n".format(usuario.nombre))
        return usuario
