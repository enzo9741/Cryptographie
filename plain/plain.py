#!/usr/bin/env python3
#coding: utf-8

# Fonction de déchiffrement via XOR repeater
# Elle prend en paramètre un texte et une clé
# Puis elle retourne le texte déchiffré
def xor_decrypt(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)

    for i in range(len(ciphertext)):
        key_char = key[i % key_length]
        decrypted_text += chr(ord(ciphertext[i]) ^ ord(key_char))

    return decrypted_text

# Séquence à déchiffrer
ciphertext_hex = "0e18091d100c11120658183a3a00055959014300085e10"


# On cherche d'abord à connaître la clé de chiffrement, on a : 
# une séquence connue car les flag sont de type guardia{flag}
# donc on a les 7 premiers octets de la séquence qu'on peut tester
# avec la fonction xor_decrypt
sequence_connu = "0e18091d100c11"
key1 = "guardia" # Car flag de type guardia{flag}

# Convertir le texte chiffré hexadécimal en une séquence d'octets
sequence_connu_chiffre = bytes.fromhex(sequence_connu)

# Déchiffrer le message avec la clé "guardia"
key = xor_decrypt(sequence_connu_chiffre.decode('utf-8'), key1)

print(f"Clé : {key}")


# Maintenant qu'on a la clé "imhotep" on peut l'utiliser
# afin de déchiffrer le reste du message
# Convertir le texte chiffré hexadécimal en une séquence d'octets
ciphertext_bytes = bytes.fromhex(ciphertext_hex)

# Déchiffrer le message avec la clé trouvée précédement
decrypted_message = xor_decrypt(ciphertext_bytes.decode('utf-8'), key)

print(f"Message déchiffré : {decrypted_message}")