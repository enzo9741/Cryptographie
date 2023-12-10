#!/usr/bin/env python3
#coding: utf-8

from Cryptodome.Cipher import AES
from Cryptodome.Util import Counter
# import os

# KEY = os.urandom(16)

# def encrypt(plaintext):
# 	cipher = AES.new(KEY, AES.MODE_CTR, counter=Counter.new(128))
# 	ciphertext = cipher.encrypt (plaintext)
# 	return ciphertext.hex()

test = b"No right of private conversation was enumerated in the Constitution. I don't suppose it occurred to anyone at the time that it could be prevented."
# print (encrypt(test))

# with open('flag.txt', 'rb') as f:
# 	flag = f.read().strip()
# 	print(encrypt(flag))
	
# ---------------------------------    
# Réponse
# On sait que communication txt comporte : 
#   - le texte "test" chiffré avec une clé inconnue
#   - le flag chiffré avec une clé inconnue
# Comme par hasard le fichier communication.txt comporte 2 lignes

# Réaliser un XOR répété
def repeating_xor(hex_str1, hex_str2):
	result = ""
	for char1, char2 in zip(hex_str1, hex_str2):
		result += hex(int(char1, 16) ^ int(char2, 16))[2:]
	return result

# Variable "test" chiffrée avec une clé inconnue
target_test = "020b7dfb9c505032f4aea799b7647732aaf68055de63d37685b07959db785e3514147a5ac147651de14a995fc4be8c65cef0f2dbbcd41c1dc1ce4d00afde838111abb3af3fd0f6f15cabe178ce69cffecee4ac5901e2cafcc794d3618ed0ee18d59bd4bcbe1b9883cc46ef6466ace9ced128ec292ba3e275e4934475a13fa5ba04c7150009bafd3f1536c202cf4978a6c437"
# print(f"Test chiffré avec clé inconnue : {target_test}")
# Flag de type guardia{blabla} chiffré avec une clé inconnue
# On a :
#   - 2b113cfb915e593d = guardia{
#   - c0 = }  
#   - b0f1afe6b3496c77bed1802af45a = flag 14 caractères
# Le flag fait donc 23 octets   
target_flag = "2b113cfb915e593db0f1afe6b3496c77bed1802af45ac0"
known_flag = b"guardia{"

# -----------------------------------------------------------------
# /!\ ATTENTION /!\
# Ce qui va suivre est le fruit de moultes réflexions et recherches 
# -----------------------------------------------------------------

# Voyons ce que ça donne quand on xor test et target_test
xor_test = repeating_xor(test.hex(), target_test)
print(f"XOR des tests : {xor_test}")

# Faisons un xor entre le target_flag et le knowflag
xor_flag = repeating_xor(known_flag.hex(), target_flag)
print(f"XOR des flag : {xor_flag}")

# Comme on a xoré sur 8 octets "guardia{"
# On remarque que les 8 premiers octets de xor_test et xor_flag sont identiques
# On en a conclu, que le xor entre le résultat chiffré et non chiffré sera 
# identique peu importe sa longueur
# On va donc xoré target_flag avec les 23 premiers octets de xor_test
# car le target_flag fait 23 octets dynamiquement avec la longueur du flag

# Longueur du flag
len_flag = int(len(target_flag)/2)

# Convertir la chaîne hexadécimale en bytes
byte_data = bytes.fromhex(xor_test)

# Récupérer les 23 premiers octets
premiers_octets = byte_data[:len_flag].hex()

# XOR des 23 premiers octets de xor_test et de target_flag
flag_hex = repeating_xor(target_flag, premiers_octets)

# Affichage du drapeau sous forme de texte
flag = bytes.fromhex(flag_hex).decode()
print(f"Flag : {flag}")