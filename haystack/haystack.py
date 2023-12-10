#!/usr/bin/env python3
#coding: utf-8

# On déclare la fonction pour le repeating key xor
def repeating_key_xor(ciphertext, key):
    decrypted = b""
    key_index = 0

    for char in ciphertext:
        decrypted_char = bytes([char ^ key[key_index]])
        decrypted += decrypted_char

        key_index = (key_index + 1) % len(key)

    return decrypted

# Afficher tous les motifs de 4 octets qui se répètent
# Car on xor le texte avec 8 octets connus : guardia{ 
def find_repeated_patterns(decrypted_text):
    seen_patterns = set()

    for i in range(len(decrypted_text) - 3):
        pattern = decrypted_text[i:i+4]
        if pattern in seen_patterns:
            print(f"Motif répété trouvé : {pattern}")
            return pattern
        else:
            seen_patterns.add(pattern)

# Charger le texte chiffré depuis le fichier
with open("haystack.txt", "r") as file:
    # Lire le contenu complet du fichier
    ciphertext = file.read().strip()
    file.seek(0)
    # Lire le fichier ligne par ligne 
    lines = file.readlines()

# Convertir le texte chiffré hexadécimal en bytes
ciphertext_bytes = bytes.fromhex(ciphertext)

test_key = b"guardia{"

# Décrypter le texte complet avec la clé de 8 octets
decrypted_text = repeating_key_xor(ciphertext_bytes, test_key)

# Recherche de patterne qui se répète 2 fois 
possible_key = find_repeated_patterns(decrypted_text)

# Afficher chaque ligne décryptée avec la clé possible
for i, line in enumerate(lines, 1):  # commencer la numérotation à partir de 1
    # Convertir la ligne chiffrée hexadécimale en bytes
    line_bytes = bytes.fromhex(line.strip())
    # Décrypter la ligne avec la clé fixe
    decrypted_line = repeating_key_xor(line_bytes, possible_key)

    # Afficher la ligne décryptée avec le numéro de ligne
    print(f"Ligne {i}: {decrypted_line.decode('latin-1')}")


# On voit Ligne 45: dia{guarm/3moy_8mC4Vk(s}b(cb~
# J'ai décidé de resester le code avec une test_key = dia{guar
# Cette réflexion a été faite après un réveil à 6h du matin sur un canapé

test_key2 = b"dia{guar"

# Décrypter le texte complet avec la nouvelle clé de 8 octets
decrypted_text = repeating_key_xor(ciphertext_bytes, test_key2)

# Recherche de patterne qui se répète 2 fois 
real_key = find_repeated_patterns(decrypted_text)

# Donc on test à la ligne 45 la possible key
flag_bytes = bytes.fromhex(lines[44])
decrypted_flag = repeating_key_xor(flag_bytes, real_key)

# Et on a le flag
print(f"La réponse est : {decrypted_flag}")