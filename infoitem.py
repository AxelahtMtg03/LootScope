import requests
from functools import lru_cache
URLDROP = "https://api.warframestat.us/drops/"
URLITEM = "https://api.warframestat.us/items/"

def normalize(s: str)->str:
    return (s or "").lower().strip()


@lru_cache(maxsize=1)
def get_drops():    
    try:
        response = requests.get(URLDROP, timeout=10)
        response.raise_for_status()  # Lève une erreur si code != 200
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Impossible de récupérer les données :", e)
        return []


def dropsearch(name_item:str)->list:
    #pour avoir les infos lieux rarete chance d'avoir
    data = get_drops()
    name_item=normalize(name_item)
    ls=[]
    dico=None
    for element in data:
        if  name_item in normalize(element.get("item")):

            dico=element
            ls.append(dico)
    return ls

def maxChance(items:list):
    if items==[]:
        return []
    max=items[0]['chance']
    for element in items:
        if element['chance']>max:
            max=element['chance']
    lsmax=[]
    for element in items:
        if element['chance']==max:
            lsmax.append(element)
    return lsmax

def trieChance(items:list):
    if items==[]:
        return []
    for i in range(len(items)):
        for j in range(i):
            if items[i]['chance']>items[j]['chance']:
                temp=items[i]
                items[i]=items[j]
                items[j]=temp
    return items

endroit = {
    "Mercury": 'Mercure.png',
    "Venus": 'Venus.png',
    "Earth": 'Terre.png',
    "Mars": 'Mars.png',
    "Phobos": 'Phobos.png',
    "Jupiter": 'Jupiter.png',
    "Saturn": 'Saturne.webp',
    "Uranus": 'Uranus.webp',
    "Neptune": 'Neptune.png',
    "Pluto": 'Pluton.png',
    "Eris": 'Eris.png',
    "Sedna": 'Sedna.png',
    "Europa": 'Europe.png',
    "Lua": 'Lua.png',
    "Ceres": 'Ceres.png',
    "Deimos": 'Deimos.webp',
    "Zariman": 'New_Zariman.webp',
    "Void": 'Void.png',
    "Duviri": 'Duviri.webp',

    "Steel Meridian": "Steel Meridian.webp",
    "Arbiters of Hexis": "Arbiters of Hexis.webp",
    "Cephalon Suda": "Cephalon Suda.webp",
    "The Perrin Sequence": "The Perrin Sequence.webp",
    "Red Veil": "Red Veil.webp",
    "New Loka": "New Loka.webp",
    "Conclave": "Conclave.webp",
    "Cephalon Simaris":"Cephalon Simaris.webp",
    "Ostrons": "Ostrons.webp",
    "The Quills": "The Quills.webp",
    "Solaris United": "Solaris United.webp",
    "Vox Solaris": "Vox Solaris.webp",
    "Ventkids": "Ventkids.webp",
    "Entrati": "Entrati.webp",
    "Necraloid": "Necraloid.webp",
    "The Hex": "The Hex.webp",
    "The Holdfasts": "The Holdfasts.webp",
    "Cavia": "Cavia.webp",
    "Kahl's Garrison": "Kahl's Garrison.webp",
    "Operational Supply": "Operational Supply.webp",
    "Nightwave": "Nightwave.webp",

    "Lith Relic": "Lith.webp",
    "Meso Relic": "Meso.webp",
    "Neo Relic": "Neo.webp",
    "Axi Relic": "Axi.webp",
    "Requiem Relic": "Requiem.webp",

    "Sanctuary Onslaught": "https://static.wikia.nocookie.net/warframe/images/3/3d/SanctuaryOnslaught.png",
    "Elite Sanctuary Onslaught": "https://static.wikia.nocookie.net/warframe/images/0/0a/EliteSanctuaryOnslaught.png",
    "Steel Path": "https://static.wikia.nocookie.net/warframe/images/d/df/SteelPath.png",
    "Arbitrations": "https://static.wikia.nocookie.net/warframe/images/3/3a/Arbitrations.png",
    "Sortie": "https://static.wikia.nocookie.net/warframe/images/4/4e/Sortie.png",
    "Kuva Fortress": 'Forteresse_Kuva.webp',
    
    "Vem Tabook":"Vem Tabook.png",
    "Shik Tal":"Shik Tal.png",
    "Leekter":"Leekter.png",
    "Proselytizer":"ZealotProselytizer.webp",
    "Herald":"ZealotHerald.webp",
    "Baptizer":"ZealotBaptizer.webp",
    "vor":"vor.png"

}
def get_place_image(place: str) -> str:
    """Retourne l'image correspondant au lieu"""
    place = place or ""
    for key, url in endroit.items():
        if key.lower().split()[0] in place.lower():  # Vérifie le mot principal
            return url
    return "https://static.wikia.nocookie.net/warframe/images/1/10/Placeholder.png"
#print(dropsearch("Valkyr"))# {'place': 'The Perrin Sequence, Partner', 'item': 'Enraged (Valkyr)', 'rarity': 'Common', 'chance': 100}