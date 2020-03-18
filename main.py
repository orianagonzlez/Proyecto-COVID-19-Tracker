from time import sleep
from colorama import init, Fore, Style
from Funciones import pedir_entero_positivo_validado
from RegistroLocal import registrar, ver

init(autoreset=True)

def separador():
    print("|"*90)

def main():
    print("Bienvenido a COVID-19 Tracker!\n")

    continuar = 1
    while continuar:
        print("Qué desea hacer?")
        print('''
    1. Realizar registro local 
    2. Ver personas en registro local
    3. Ver estadísticas
    4. Finalizar programa
    ''')

        accion = pedir_entero_positivo_validado("Seleccione una opción: ")
        while accion < 1 or accion > 4:
            accion = pedir_entero_positivo_validado("Seleccione una opción: ")

        if accion == 1:
            separador()
            print(registrar())           
        elif accion == 2:
            separador()   
            ver()      
        elif accion == 3:
            separador()
        else:
            print("\n\nHasta luego. Recuerde tomar sus previsiones!")
            separador()
            continuar = 0
        
main()