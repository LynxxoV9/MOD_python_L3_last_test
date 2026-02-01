# Projet de fin de module Python – Licence 3 🔥

Ce projet a été conçu et testé dans un environnement **Windows 10** dans le cadre du module Python en Licence 3 Informatique (Développement et Sécurité) à l’ESA Togo.

Il est composé de deux parties principales :  
le scraping d’un site web local et la mise en œuvre d’une logique de gestion de stock.

## Encadrement académique

Module : Python  
Enseignant : Ing. GBADAMASSI ABDOU-AKIM  
Fonction : Senior Software Engineer, Consultant informatique CCI TOGO

## Description du projet

### Partie 1 : Scraping web local 💻

Cette partie consiste à analyser et extraire les éléments d’un site web cloné en local :
- Titres (h1, h2, h3)
- Paragraphes
- Liens
- Formulaire
- Images

Les données extraites sont :
- enregistrées dans un fichier texte `collector.txt`
- les images sont copiées dans un dossier `IMG_collector`

Le scraping est réalisé à l’aide de BeautifulSoup après récupération du code HTML via une requête HTTP locale.

### Partie 2 : Gestion de stock 📦

Cette partie met en œuvre la logique d’une application de gestion de stock :
- Ajout de produits
- Modification des quantités
- Vérification des seuils critiques
- Affichage de l’inventaire

Les données sont stockées dans un dictionnaire Python structuré.

## Prérequis ⚠️

Avant d’exécuter le projet, il est nécessaire d’avoir :
- Un environnement principal de développement (Win 10 pour nous)
- Python 3.9 ou supérieur
- Serveur local XAMPP ou équivalent
- Modules Python suivants installés :
  - requests
  - beautifulsoup4
  - html5lib

## Installation des dépendances :

    pip install requests beautifulsoup4 html5lib


Attention selon le système d’exploitation

Ce projet a été développé sous Windows 10.

Pour les utilisateurs sous Linux ou macOS :

    La commande os.system("cls") doit être remplacée par clear

    Les chemins absolus Windows (C:\xampp\...) doivent être adaptés

    Les séparateurs de chemins doivent respecter l’OS utilisé

Une adaptation manuelle est donc nécessaire pour garantir le bon fonctionnement.
Exécution du projet

    Démarrer le serveur local (XAMPP)

    Placer le site cloné dans le dossier htdocs

    Lancer le script Python principal :

python main.py

    Vérifier les fichiers générés :

    collector.txt

    dossier IMG_collector

Objectifs pédagogiques 🎯

Ce projet permet de :

    Manipuler des fichiers et des données web

    Comprendre le fonctionnement du scraping

    Appliquer des structures de données

    Mettre en pratique une logique applicative

    Consolider les bases du langage Python

## Auteur

Team: *LIVE_SCRAPERS*

Membre:

FIABI Kokou Olivier - Sécurité Informatique

NANGA Ditorga       - Génie Logiciel

LAKEMATE Jean       - Génie Electrique

NBINDIGOUM Israël  - Génie Logiciel

*Licence 3 – Ecole Supérieure des Affaires - Togo*
