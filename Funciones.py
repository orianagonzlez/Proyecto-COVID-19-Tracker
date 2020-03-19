from colorama import init, Fore, Style

init(autoreset=True)

def validar_entero_positivo(n):
    '''
    Función para verificar si el argumento pasado es un numero entero positivo. 

    Retorna verdadero si se cumple dicha condición y falso de lo contrario.
    '''
    es_entero = False
    try:
        int(n)
        if int(n) >= 0:
            es_entero = True
    except:
        es_entero = False
    return es_entero

def pedir_entero_positivo_validado(mensaje):
    '''
    Función para pedir un numero hasta que el usuario ingrese un valor que sea un numero entero positivo.

    Retorna el valor ingresado como int.
    '''
    n = input(mensaje)
    while not validar_entero_positivo(n):
        n = input(mensaje)
    return int(n)

def separador():
    print("\n")
    print(Fore.BLUE + "▪ "*80)
    print("\n")