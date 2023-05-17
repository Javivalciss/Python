import urllib.parse      #Importamos Modulos necesarios 
import requests          #Importamos Modulos necesarios 
import json              #Importamos Modulos necesarios 


main_api="https://mapquestapi.com/directions/v2/route?"   #Variable de la URL base de la API de MapQuest
key="1fc0TABJ7bbDfHhrbDzeIGPMY6iaRtnR"                    #Clave de API de MapQuest
locale="es_ES"                                            #Configurar idioma 
unit = "k"                                                #Configurar la unidad de distancia en kilómetros

while True:           #Creamos un Bucle para que vuelva a solicitar ciudades  después de mostrar la información
    origen= input("Ingrese Ciudad de Origen : ")              # Solicitar al usuario la ciudad de origen
    if origen.lower() =="s" or origen.lower() == "salida":    #Si se coloca s  o salida que quiebra el bucle y se cierra
        break
        break

    destino= input ("Ingrese Ciudad de Destino : ")            #Solicitar al usuario la ciudad de destino
    if destino.lower() == "s" or destino.lower() == "salida":  #Si se coloca s  o salida que quiebra el bucle y se cierra
        break

    url = main_api + urllib.parse.urlencode({"key":key, "from" : origen,"to":destino,"unit":unit, "locale" :locale }) # Construir la URL completa de la solicitud de la ruta utilizando la función urlencode para codificar los parámetros
    json_data = requests.get(url).json()                    #Realizar la solicitud GET a la API de MapQuest y obtener la respuesta en formato JSON

    distance = json_data["route"]["distance"]               #Obtener la distancia de la ruta desde la respuesta JSON
    distance_decimal = round(distance, 1)                   #Redondear la distancia a un decimal

    time = json_data["route"]["formattedTime"]              #Obtener el tiempo de viaje formateado desde la respuesta JSON
    narrative = json_data["route"]["legs"][0]["maneuvers"]  #Obtener la narrativa del viaje desde la respuesta JSON

    print("Distancia:", distance ,"Km")   # Imprimir la distancia de la ruta
    print("Tiempo de viaje:", time)       # Imprimir la distancia de la ruta
    print("Narrativa del viaje:")         # Imprimir el encabezado de la narrativa del viaje

    for step in narrative:
        print("- ", step["narrative"])   # Recorrer cada paso de la narrativa e imprimirlo con un guion (-)





