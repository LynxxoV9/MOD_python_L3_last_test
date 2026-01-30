import os
import shutil  #Pour copier les images dans le collecteur d'images
import requests
from bs4 import BeautifulSoup
#from urllib.parse import urljoin                #Pour reconstituer les urls des images ici
import time                 # Amélioration pour un peut d'interaction


def get_source(image):
    return image.get("src") or image.get("data-src")


os.system("cls")                #nettoyage du terminal sous à modifier ...cls par selon son os clear for linux for exemple
"""Début du scrapping"""
print("\n\nQuelques secondes ...\n\n")
#lien vers le site cible
url = "http://localhost/MOD_python_L3_last_test/"
# récupération du code source
crop = requests.get(url)
html_ = crop.text
#2s sleeping
time.sleep(2)
print("A moment please, parsing starts...\n")
crop_soup = BeautifulSoup (html_,"html5lib")                 #Interprétation du code source récupéré

titre_level1 = crop_soup.find("h1").text                # Récupération du grand titre 

titre_level2 = crop_soup.find_all("h2")                 #récupération des titres 2

titre_level3 = crop_soup.find_all("h3")                 #récupération des titre 3

paragraphe = crop_soup.find_all("p")                #récupération des par(agraphes)

links_ = crop_soup.find_all("a")                #Ici on a pas encore d'lien juste la balise a

formulaire = crop_soup.find("form")                 #Récupération du formulaire



#les images sont dans apropos.html... let' open it
with open("apropos.html","r",encoding="utf-8") as F:
    apropos = F.read()
F.close()
apropo_soup = BeautifulSoup(apropos,"html5lib")
images = apropo_soup.find_all("img")
#Récupération des liens absolus
"""absolu_urls =[]
for img in images:
    source_ = get_source(img)
    if not source_:
        continue

    absolu_url = urljoin(url,source_)
    absolu_urls.append(absolu_url)
"""
### Vu que le site est en local nous allons juste récupérer les chemins absolus vers les
# les images et les copier avec la commande cp dans un dossier IMG_collector !
# On devrait modifier cette partie pour renseigner le bon chemin selon son OS
try:
    os.mkdir(r"c:\xampp\htdocs\MOD_python_L3_last_test\IMG_collector")
except FileExistsError:
    pass

for img in images:
    base = os.path.basename(img.get("src"))
    complet_base_source = os.path.join("assets",base)
    complet_base_destination = os.path.join("IMG_collector",base)
    shutil.copy(complet_base_source,complet_base_destination)


#slepping 2
time.sleep(2)
print("Now we collect, a moment please !")
time.sleep(3)


#Collector : Le fichier text qui va récupérer/collecter les données
collector = open("collector.txt","w+")
collector.write(f"TITcRE 1:\n{titre_level1}\n\nTITRE 2:\n")
 # ajout des titres 2 collector
for titre2 in titre_level2:
    collector.write(f"{titre2.text}\n")

# ajout des Titre 3 s'ils existent
collector.write("\nTITRE 3:\n")
for titre3 in titre_level3:
    collector.write(f"{titre3.text}\n")

# ajout des paragrphes
collector.write("\nPARAGRAPHES:\n")
compter = 0
for para in paragraphe:
    compter += 1
    collector.write(f"Paragraphe[{compter}]:\n{para.text.strip()}\n")

#Ajout des liens vers une destination dans collector
collector.write("\nLIENS:\n")
for lien in links_:
    collector.write(f"///-Le lien vers [{lien.text}]: {lien.get("href")}\n")

collector.write(f"\nFORMULAIRE:\n {formulaire} \n")

# fin du fichier
collector.close()

#Count count
time.sleep(1)
print("\t \t 40% done\n")
time.sleep(1)
print("\t \t 70% done\n")
time.sleep(1)
print("\t \t 100% done\n")
time.sleep(2)

print ("\n\n \t\t\t\t ==========| Now check collector.txt and IMG_collector !!! |==========")

print("\n \n \n\t\t\t__________-------------------------[by LIVE_SCRAPERS]-------------------------__________\n\n\n")
