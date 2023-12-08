# Dans ce code j'ai testé la clé trouvée dans test.py
# J'ai également rajouter une suite à ce test mais sans succès
# Voyez ce que vous pouvez en tirer.


def xor_decrypt(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)

    for i in range(len(ciphertext)):
        key_char = key[i % key_length]
        decrypted_text += chr(ord(ciphertext[i]) ^ ord(key_char))

    return decrypted_text

ciphertext = "0e18091d100c11120658183a3a00055959014300085e10"
known_sequence = "0e18091d100c11"
base_key = "ujtur"    

# Tester la clé "ujtur"
decrypted_message = xor_decrypt(ciphertext, base_key)
print(f"Clé : {base_key}")
print(f"Message déchiffré : {decrypted_message}")

# Tester la clé avec la table ASCII pour un dernier caractère
for i in range(128):  # Tester les caractères ASCII de 0 à 127
    key = base_key + chr(i)
    decrypted_message = xor_decrypt(ciphertext, key)
    
    # Vérifier si le message déchiffré correspond à la séquence connue
    if decrypted_message.lower().startswith(known_sequence.lower()):
        print(f"Clé trouvée : {key}")
        print(f"Message déchiffré : {decrypted_message}")
        break
