#!/usr/bin/env python3
#coding: utf-8

import socket
import re
import string

HOST='ctfd.lasne.pro'
PORT=1337

# variable socket globale
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Helper functions

# Connect to the server
def connect():
	s.connect((HOST, PORT))
	s.settimeout(5.0)

	return s

# Recieve data
def receive():
	data = s.recv(2048)

	return data

# Recieve data until a keyword
def receive_until(delimiter):
	connection_data = b''

	while True:
		data = s.recv(2048)
		connection_data += data

		if delimiter in connection_data:
			return connection_data

# Send data
def send(data):
	if type(data) != bytes:
		print('Cette fonction envoie uniquement un type \'bytes\'')
		return None

	s.send(data)

#Fonction permet de calculer un score pour savoir si il s'agit d'un mot
#Il utilise la frequence a laquelle apparait une lettre dans un mot
def score_english(plaintext):
	#Tableau contenant la lettre ainsi que ça fréquence d'apparition
	#Le tableau contient aussi des character speciaux avec un malus
	letter_frequency = {'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 
								's': 6.33, 'h': 6.09,'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 
								'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23, 'g': 2.02, 'y': 1.97, 
								'p': 1.93, 'b': 1.49, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15,
								'q': 0.10, 'z': 0.07, '~': -100, '}': - 100, '{': -100, '|': -100, 
								'@': -100, '^': -100, '=': -100, '`': -100, ']': -100, '\\': -100}  
    
	#Passage en minuscule du mot
	plaintext_lower = plaintext.lower()

	#Calcul du score
	score = sum(letter_frequency.get(char, 0) for char in plaintext_lower)

	#Retour du score
	return score

#Decode une chaine avec un octect Xoré
def decode(string):
	#Prévension des exception en cas d'erreur lors du decodage
	try:
		string_decode = bytes.fromhex(string).decode()
	except UnicodeDecodeError as e:
		#print(f"Error decoding bytes: {e}")
		return
	else: 
		#Parcours des octect de 90 a 150
		for i in range(255):
			value = ''
			#Parcours de chaque caractere a déchiffrer
			for caractere in string_decode:
				#Xor du caractere
				test = ord(caractere) ^ i
				if test > 255:
					test = 0 + test-255
				#Ajout de la lettre trouvé
				value += chr(test)
				#Récupération du scord
				score = score_english(value)

				#Filtre affin de vérifier le score du mot
				if score > 50:
					#Affichage de la valeur trouvé
					#print(f"{value} | {score_english(value)} | {test} | {i}")

					#Envoie du code trouvé
					send(value.encode())
					result = receive()
					if b"guardia" in result:
						#Affichage du flag reçu
						print(result)


if __name__ == '__main__':
	
	# connexion au challenge
	# et reception du flag
	connect()
	data = receive_until(b'Code:')
	print(data.decode())

	print("========================")

	# <----> Le Flag
	hex_chall = data.splitlines()[3]
	print(hex_chall.decode())
	
	# Todo: décodez le flag !
	decode(hex_chall.decode())
	print("Si le flag ne s'affiche pas relancer le script jusqu'a se que le flag soit afficher")