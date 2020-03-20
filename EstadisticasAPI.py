import requests
from colorama import init, Fore, Style
from Funciones import pedir_entero_positivo_validado, separador

init(autoreset=True)

def pedir_datos():
    '''
    Función que solicita la información acerca del COVID-19 del API y la retorna como un diccionario.
    '''

    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country":""}

    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "9dadda6754msh2b5903a9c34495cp108ba5jsn3696139a67e9"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    dic = response.json()
    return dic


def organizar_datos():
    '''
    Función que agrega en una lista la información de interés de cada país del diccionario de datos sobre el COVID-19 obtenido del API.

    Retorna una lista de listas, donde cada lista sigue el siguiente formato: [pais, numero_infectados, numero_muertes, numero_recuperados].
    '''
    respuesta = pedir_datos()
    
    lista_paises = []  
    for item in respuesta['data']['covid19Stats']:
        if lista_paises == []:
            lista_paises.append([item['country'], item['confirmed'], item['deaths'], item['recovered']])
        else:
            encontrado = False
            
            for pais in lista_paises:
                if pais[0] == item['country']:
                    encontrado = True
                    pais[1] += item['confirmed']
                    pais[2] += item['deaths']
                    pais[3] += item['recovered']
                
            if not encontrado:
                lista_paises.append([item['country'], item['confirmed'], item['deaths'], item['recovered']])

    return lista_paises

def imprimir_paises():
    '''
    Función que imprime los países que tienen datos disponibles.
    '''
    lista_paises = organizar_datos()

    print("\nEl país no fue encontrado. Lista de países con datos disponibles:\n")
    for pais in lista_paises:
        print("\t-", pais[0])

def buscar_pais(pais):
    '''
    Función que toma como argumento un país, lo busca en la lista de listas con los datos de todos los países y retorna los datos 
    del país si lo encuentra y el mensaje "No encontrado" en caso contrario.
    '''
    lista_paises = organizar_datos()
    
    for item in lista_paises:
        if item[0] == pais:
            return item 
    return "No encontrado"
    
def busqueda():
    '''
    Función que busca los datos del país ingresado por el usuario. Si lo encuentra imprime el numero de infectados, muertos y recuperados,
    de lo contrario muestra una lista de los países disponibles y solicita otro país.
    '''
    pais = input("Ingrese el nombre en inglés del país que desea buscar. ***Es importante el uso de mayúsculas y minúsculas***: ")
    datos_pais = buscar_pais(pais)
    while datos_pais == "No encontrado":
        imprimir_paises()
        pais = input("\nPor favor ingrese el nombre en ingles del país que desea buscar. ***Es importante el uso de mayúsculas y minúsculas***: ")
        datos_pais = buscar_pais(pais)
    
    print(Fore.MAGENTA + "\n" + datos_pais[0] + ":\n")
    print(Fore.CYAN + "\t• Cantidad de personas infectadas:", datos_pais[1])
    print(Fore.CYAN + "\t• Cantidad de muertes registradas:", datos_pais[2])
    print(Fore.CYAN + "\t• Cantidad de personas recuperadas:", datos_pais[3])

def top10(string):
    '''
    Función que recibe como argumento el top deseado (infectados, muertos o recuperados) e imprime los 10 países con mayor cantidad 
    de personas que cumplen esa característica.
    '''
    if string == "infectados":
        indice = 1
    elif string == "muertos":
        indice = 2
    else:
        indice = 3
    
    lista_paises = organizar_datos()
    lista_paises.sort(key= lambda pais: pais[indice], reverse=True)

    for i, pais in enumerate(lista_paises[:10], 1):
        print(Fore.YELLOW + Style.NORMAL + "\t" + str(i) +".", end="") 
        print("\t" + pais[0] + ": " + str(pais[indice]) + " " + string + "\n")

def estadisticas():
    '''
    Función que permite al usuario ver las estadísticas solicitadas (de un país en específico, los 10 de países con más infectados, 
    con más muertes o con más recuperados).
    '''
    print(Fore.MAGENTA + "Qué desea hacer?")
    print('''
    1. Búsqueda de estadísticas de un país 
    2. Ver los 10 de países con más infectados
    3. Ver los 10 de países con más muertes
    4. Ver los 10 de países con más recuperados
''')

    accion = pedir_entero_positivo_validado("Seleccione una opción: ")
    while accion < 1 or accion > 4:
        accion = pedir_entero_positivo_validado("Opción inválida. Seleccione una opción: ")

    if accion == 1:
        separador()
        busqueda()
    elif accion == 2:
        separador()
        print(Fore.CYAN + "Países con más infectados por COVID-19:\n\n")
        top10("infectados")
    elif accion == 3:
        separador()
        print(Fore.CYAN + "Países con más muertes por COVID-19:\n\n")
        top10("muertos")
    else:
        separador()
        print(Fore.CYAN + "Países con más recuperados por COVID-19:\n\n")
        top10("recuperados") 
