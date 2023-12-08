# Dans ce code, je prends le début de la séquence
# et je le compare avec le début du flag qui est guardia{
# pour essayer de comprendre la clé
# Exécuter ce code pour voir la clé qui n'a pas l'air d'être la clé
# Donc ça m'énerve j'ai ragequit

# La séquence hexadécimale
sequence_connu = "0e18091d100c1112"

# Convertir la chaîne hexadécimale en une séquence d'octets
sequence_octets = bytes.fromhex(sequence_connu)

# Obtenir les valeurs ASCII pour chaque entier dans la séquence connue
valeurs_ascii_sequence = list(sequence_octets)

# La chaîne "guardia{"
chaine_guardia = "guardia{"

# Obtenir les valeurs ASCII pour chaque caractère de la chaîne "guardia{"
valeurs_ascii_guardia = [ord(char) for char in chaine_guardia]

# Additionner les valeurs ASCII des deux chaînes index par index
somme_index_par_index = [v_seq + v_guardia for v_seq, v_guardia in zip(valeurs_ascii_sequence, valeurs_ascii_guardia)]

print("Somme index par index des valeurs ASCII de la séquence connue et de la chaîne 'guardia{':", somme_index_par_index)

print("Texte résultant des valeurs ASCII sommées index par index :", ''.join(chr(somme) for somme in somme_index_par_index))
