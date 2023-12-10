#!/usr/bin/env python3
#coding: utf-8

# On sait que le texte est en base 64 car :
# - Mario 64
# - Vous n'avez pas les bases
# On sait qu'il va falloir le décoder plusieurs fois car : 
# - Inception
# On sait que le flag comporte la notion "guardia"

# Importe la bibliothèque "base64" car on va avoir besoin de l'utiliser
import base64

# Le texte que comporte le flag
texte_recherche = "guardia"

# On récupère notre fichier à déchiffrer
file_path = 'mario64.txt'
with open(file_path, 'r') as f:
    texte = f.read()

# La boucle permet de décoder le texte en base 64
# jusqu'à ce que le texte comporte le mot "guardia"
while texte_recherche not in texte:
    # Pour décoder notre texte, il faut l'encoder
    # pour que le programme comprenne qu'il s'agit
    # d'un texte en base 64 puis le décoder
    # afin de l'afficher et de pouvoir le repasser
    # dans la boucle si faux
    texte = base64.b64decode(texte.encode()).decode()

# On affiche le flag
print(texte)
 