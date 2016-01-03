#! /usr/bin/python3.4

# Main file for AES
import subBytes, mixColumns, aes_base, shiftRows, segmess, addRoundKey


# !!! Bug !!! ShiftRows renvoie simplement le message passé en paramètre (regarde dans les print de DEBUG)
# AddRoundKey bug, je comprend pas trop =/

def aes():

	M_SIZE = 4
	msg = "plain.txt"
	key_size = 256

	m = segmess.segmess(msg)
	m_size = len(m)

	print("Encrytpion for %s" % (msg))

	# Tempo array definition
	c1 = m
	c2 = m
	c3 = m
	c4 = m

	# SubBytes:
	for cpt in range(m_size):
		c1[cpt] = subBytes.subBytes(m[cpt])

	# ShiftRows:
	for cpt in range(m_size):
		c2[cpt] = shiftRows.shiftRows(c1[cpt], key_size)
	
	# MixColumns:
	for cpt in range(m_size):
		c3[cpt] = mixColumns.mixColumns(c2[cpt])

	# DEBUG
	print(c1)
	print(c2)
	print(c3)

	# AddRoundKey:
	for cpt in range(m_size):
		c4 = addRoundKey.addRoundKey(c3, key_size)

	print("Encrypted message:")
	print(c4)

