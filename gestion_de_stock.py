# {
#     "nom" : [quantite, prix_unitaire],
# }
stock = {
    "Pomme" : [50, 60],
    "Orange" : [40, 13]
}
# Ajouter un produit dans le stock
def ajouter_produit(nom, quantite, prix):
    stock[nom] = [quantite, prix]
    print(f"Produit '{nom}' ajouté avec succès")

# Modifier un produit

def modifier_stock(nom, quantite_changement):
    if nom in stock:
        stock[nom][0] += quantite_changement
        print(f"Stock de '{nom}' mis à jour avec succès")
    else:
        print("Erreur , produit nom trouvé")

# Pour vérifier les alertes

def verifier_stock(seuil=15):
    print("Stock inférieur au seuil :")
    for nom, infos in stock.items():
        if infos[0] < 15:
            print("Le produit '{nom}' est presque fini, ({infos[0]}) restants ")

# Afficher l'inventaire

def afficher_inventaire():
    print("Inventaire complet")
    for nom, infos in stock.items():
        print(f"Produit : {nom} | Quantité : {infos[0]} | Prix : {infos[1]}")
        print("\n")
    
    
# Tests d'essai

#Test d'ajout 
ajouter_produit("Banane", 100, 25)   

#Test de modification
modifier_stock("Pomme", +10)

# #Test de vérification de stock
verifier_stock("Pomme")

#Afficher inventaire
afficher_inventaire()