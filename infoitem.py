import requests
from functools import lru_cache
URLDROP = "https://api.warframestat.us/drops/"
URLITEM = "https://api.warframestat.us/items/"

def normalize(s: str)->str:
    return (s or "").lower().strip()

@lru_cache(maxsize=1)
def get_items():
    return requests.get(URLITEM).json()

@lru_cache(maxsize=1)
def get_drops():
    return requests.get(URLDROP).json() 

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
    for i in range(len(items)):
        for j in range(i):
            if items[i]['chance']>items[j]['chance']:
                temp=items[i]['chance']
                items[i]['chance']=items[j]['chance']
                items[j]['chance']=temp
    return items

    