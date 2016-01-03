#! /usr/bin/python3.4

# Main file for AES
import subBytes, mixColumns, aes_base, shiftRows, segmess, addRoundKey


# !!! Bug !!! ShiftRows renvoie simplement le message passé en paramètre (regarde dans les print de DEBUG)
# AddRoundKey bug, je comprend pas trop =/

def aes():

	M_SIZE = 4
	msg = "plain.txt"
	key_size = 256
	key = [[184, 18, 29, 158], [123, 45, 253, 202], [254, 124, 64, 32], [86, 54, 48, 68]]

	m = segmess.segmess(msg)
	m_size = len(m)

	print("Encrytpion for %s" % (msg))
	print(m)

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

	# AddRoundKey:
	for cpt in range(m_size):
		c4[cpt] = addRoundKey.addRoundKey(c3[cpt], key)

	print("Encrypted message:")
	print(c4)

	# Inversion:
	mc1 = m
	mc2 = m
	mc3 = m
	mc4 = m

	# InvAddRoundKey:
	for cpt in range(m_size):
		mc1[cpt] = addRoundKey.addRoundKey(c4[cpt], key)
	
	# InvMixColumns:
	for cpt in range(m_size):
		mc2[cpt] = mixColumns.invMixColumns(c1[cpt])

	# InvShiftRows:
	for cpt in range(m_size):
		mc3[cpt] = shiftRows.invShiftRows(mc2[cpt], key_size)
	
	# InvSubBytes:
	for cpt in range(m_size):
		mc4[cpt] = subBytes.invSubBytes(mc3[cpt])

	print("Uncrypted message:")
	print(mc4)
