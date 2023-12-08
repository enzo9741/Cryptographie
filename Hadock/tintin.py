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

#
def score_english(plaintext):
	english_letter_frequency = {'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 
								's': 6.33, 'h': 6.09,'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 
								'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23, 'g': 2.02, 'y': 1.97, 
								'p': 1.93, 'b': 1.49, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15,
								'q': 0.10, 'z': 0.07, '~': -100, '}': - 100, '{': -100, '|': -100, 
								'@': -100, '^': -100, '=': -100, '`': -100, ']': -100, '\\': -100}  
    
	plaintext_lower = plaintext.lower()
	score = sum(english_letter_frequency.get(char, 0) for char in plaintext_lower)

	return score

#Decode
def decode(string):
	try:
		string_decode = bytes.fromhex(string).decode()
	except UnicodeDecodeError as e:
		#print(f"Error decoding bytes: {e}")
		return
	else: 
		for i in range(90, 150):
			test2 = ''
			for caractere in string_decode:
				test = ord(caractere) ^ i
				if test > 255:
					test = 0 + test-255
				test2 += chr(test)
				score = score_english(test2)
				if score > 70:
					print(f"{test2} | {score_english(test2)} | {test} | {i}")
					send(test2.encode())
					print(receive())


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

	# Envoi du code
	send('Moule à Gauffffrre !'.encode())
	print(receive())