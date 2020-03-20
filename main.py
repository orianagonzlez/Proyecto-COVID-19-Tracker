from time import sleep
from colorama import init, Fore, Style
from Funciones import pedir_entero_positivo_validado, separador
from RegistroLocal import registrar, ver
from EstadisticasAPI import estadisticas

init(autoreset=True)

def main():
    '''
    Función que controla el flujo de todo el programa (registrarse, ver el registro local, ver estadísticas y finalizar).
    '''
    separador()
    print(Fore.MAGENTA + '''
         ██████╗ ██████╗ ██╗   ██╗██╗██████╗        ██╗ █████╗     ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
        ██╔════╝██╔═══██╗██║   ██║██║██╔══██╗      ███║██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
        ██║     ██║   ██║██║   ██║██║██║  ██║█████╗╚██║╚██████║       ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
        ██║     ██║   ██║╚██╗ ██╔╝██║██║  ██║╚════╝ ██║ ╚═══██║       ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
        ╚██████╗╚██████╔╝ ╚████╔╝ ██║██████╔╝       ██║ █████╔╝       ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
         ╚═════╝ ╚═════╝   ╚═══╝  ╚═╝╚═════╝        ╚═╝ ╚════╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   
            ''')

    #Bucle que asegura que se vuelva al menu principal a menos de que el usuario indique lo contrario
    continuar = 1
    while continuar:
        separador()
        print(Fore.MAGENTA + "Qué desea hacer?")
        print('''
    1. Realizar registro local 
    2. Ver personas en registro local
    3. Ver estadísticas (necesita acceso a Internet)
    4. Finalizar programa
    ''')

        accion = pedir_entero_positivo_validado("Seleccione una opción: ")
        while accion < 1 or accion > 4:
            accion = pedir_entero_positivo_validado("Opción inválida. Seleccione una opción: ")

        if accion == 1:
            separador()
            print(registrar()) 
            sleep(2)          
        elif accion == 2:
            separador()   
            ver()
            sleep(2)      
        elif accion == 3:
            separador()
            estadisticas()
            sleep(2)
        else:
            print(Fore.CYAN + "\n\nHasta luego. Recuerde tomar sus previsiones!")
            separador()
            continuar = 0
        
main()