import requests
import json
import urllib.parse

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "flGOsvQMZUKwnnQ832gInX7Vha9EEIfh"
translation_api = "https://api.mymemory.translated.net/get?"

def translate_text(text, target_language):
    url = translation_api + urllib.parse.urlencode({"q": text, "langpair": "en|" + target_language})
    response = requests.get(url).json()
    if "responseStatus" in response and response["responseStatus"] == 200:
        return response["responseData"]["translatedText"]
    else:
        return None

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
    for each in json_data["route"]["legs"][0]["maneuvers"]:
        narrative = each["narrative"]
        translated_text = translate_text(narrative, "es")
        if translated_text is not None:
                print(translated_text + " (" + str("{:.2f}".format(each["distance"] * 1.61)) + "km)")
        else:
                print(narrative + " (" + str("{:.2f}".format(each["distance"] * 1.61)) + "km)")
    print("=============================================\n")

