import requests
import json

API_KEY = "AIzaSyCyjABmSvZqZko9TqXoeCaZDKIpeFlyxJo"
CX = "3783d824f026844e6"

query = "les meilleures séries Netflix 2025"
url = "https://www.googleapis.com/customsearch/v1"

params = {
    "key": API_KEY,
    "cx": CX,
    "q": query
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    with open("resultats.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Fichier JSON généré !")
else:
    print("Erreur :", response.status_code, response.text)
