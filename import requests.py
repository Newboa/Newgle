import requests
import json
import time

# Variables
API_KEY = 'AIzaSyCyjABmSvZqZko9TqXoeCaZDKIpeFlyxJo'  # Remplace par ta clé API
CX = '3783d824f026844e6'  # Remplace par ton ID de moteur de recherche
BASE_URL = "https://www.googleapis.com/customsearch/v1"

# Fonction pour récupérer des résultats de recherche
def fetch_search_results(query):
    params = {
        'key': API_KEY,
        'cx': CX,
        'q': query,
        'num': 10  # Nombre de résultats par requête (max 10)
    }
    
    # Requête à l'API Google Custom Search
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data['items'] if 'items' in data else []
    else:
        print(f"Erreur {response.status_code}: {response.text}")
        return []

# Liste de recherches populaires
queries = [
    "meilleures pratiques JavaScript",
    "nouvelles technologies IA 2025",
    "comment apprendre Python",
    "réduire son empreinte carbone",
    "les tendances de la mode 2025",
    "résultats coupe du monde 2024",
    "nouvelles tendances en biotechnologie",
    "révolution énergétique verte",
    "cinéma : films à voir",
    "les livres les plus vendus 2025"
]

# Liste pour stocker les résultats
all_results = []

# Récupérer des résultats pour chaque requête
for query in queries:
    print(f"Recherche pour: {query}")
    search_results = fetch_search_results(query)
    
    # Ajouter les résultats à la liste
    for result in search_results:
        all_results.append({
            "title": result['title'],
            "url": result['link'],
            "snippet": result['snippet'],
            "query": query
        })
    
    # Attendre 1 seconde pour éviter de dépasser les limites d'API
    time.sleep(1)

# Sauvegarder les résultats dans un fichier JSON
with open('search_results.json', 'w', encoding='utf-8') as f:
    json.dump(all_results, f, indent=4, ensure_ascii=False)

print(f"Base de données JSON générée avec {len(all_results)} résultats.")
