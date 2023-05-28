import requests
import json
import urllib.parse

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "flGOsvQMZUKwnnQ832gInX7Vha9EEIfh"

while True:
    orig = input("Ciudad de Origen: ")
    if orig == "s":
        break
    dest = input("Ciudad de Destino: ")
    if dest == "s":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Direccion desde " + (orig) + " hacia " + (dest))
        print("Duracion del viaje:  " + (json_data["route"]["formattedTime"]))
        print("Kilometros:  " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("=============================================")
