import requests
from colorama import init, Fore, Style
from Funciones import pedir_entero_positivo_validado, separador

init(autoreset=True)

def pedir_datos():
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

def buscar_pais(pais):
    paises = organizar_datos()
    
    for item in paises:
        if item[0] == pais:
            return item 
        else:
            return "No encontrado"
    
def busqueda():
    pais = input("Ingrese el nombre en ingles del pais que desea buscar: ").title()
    datos_pais = buscar_pais(pais)
    while datos_pais == "No encontrado":
        pais = input("El pais no fue encontrado. Por favor ingrese el nombre en ingles del pais que desea buscar: ").title()
        datos_pais = buscar_pais(pais)
    
    print("\n" + datos_pais[0] + ":")
    print("\t• Cantidad de personas infectadas:", datos_pais[1])
    print("\t• Cantidad de muertes registradas:", datos_pais[2])
    print("\t• Cantidad de personas recuperadas:", datos_pais[3])

def top10(string):
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
    print(Fore.MAGENTA + "Qué desea hacer?")
    print('''
    1. Busqueda de estadisticas de un pais 
    2. Ver top 10 de paises segun infectados
    3. Ver top 10 de paises segun muertes
    4. Ver top 10 de paises segun recuperados
''')

    accion = pedir_entero_positivo_validado("Seleccione una opción: ")
    while accion < 1 or accion > 4:
        accion = pedir_entero_positivo_validado("Seleccione una opción: ")

    if accion == 1:
        separador()
        busqueda()
    elif accion == 2:
        separador()
        print(Fore.CYAN + "Paises con mas infectados por COVID-19:\n\n")
        top10("infectados")
    elif accion == 3:
        separador()
        print(Fore.CYAN + "Paises con mas muertes por COVID-19:\n\n")
        top10("muertos")
    else:
        separador()
        print(Fore.CYAN + "Paises con mas recuperados por COVID-19:\n\n")
        top10("recuperados") 
