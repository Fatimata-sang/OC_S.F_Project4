## Programme de gestion de tournoi d'échecs

## Projet n°4 - Développez un programme logiciel en Python

## Présentation du programme

Ce programme est destiné à gérer le déroulement d'un tournoi de jeu d'échecs.

Il est doté de plusieurs fonctionnalités et notamment :

-La création de joueurs et de tournois.

-La gestion du déroulé d'un tournoi.

-L'affichage de rapports divers (attention, il faut avoir généré des données au préalable en utilisant le programme pour afficher les rapports).

## Installation des logiciels requis

Ce programme a été développé en utilisant la version 3.10.11 de Python 

## Création et activation de l'environnement virtuel

## Cloner le projet

```
git clone https://github.com/Fatimata-sang/P7_SANGARE_Fatimata_Fatim.git
```
## Créer un environnement virtuel

```
python -m venv env 
``` 
## Activation de l'environnement virtuel MacOs et Linux

```
source env/bin/activate
```
## Activation de l'environnement virtuel Windows

```
env\Scripts\activate 
```

## Installation de toutes les dépendances avec `pip`

```
pip install -r requirements.txt
```

## Exécution du script

Veuillez exécuter le fichier main.py avec la commande suivante :

````
python main.py
````

## Notes importantes

a) Il est PRIMORDIAL de créer 8 joueurs au préalable avant de créer un tournoi.
b) Pour créer les joueurs, sélectionnez l'option[1]dans le menu principal, puis laissez-vous guider.
c) Une fois les 8 joueurs créés, il faut créer le tournoi.
d) Pour créer un tournoi, revenez dans le menu principal puis sélectionnez l'option[2], puis laissez-vous guider.
e) Une fois le tournoi créé, vous pourrez commencer le tournoi en sélectionnant l'option dédiée dans le menu Tournoi. 

## Génération d'un rapport Flake8 - HTML

Dans la racine du dossier, veuillez exécuter la commande suivante dans le terminal : 

````
 flake8 --format=html --htmldir=flake8-report 
 
````
