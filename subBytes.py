#! /usr/bin/python3.4

# First function in AES: SubBytes (substitution)
# Bi,j = SubBytes(Mi,j) = A x Mi,j^-1 XOR c

# Array manipulation
import aes_base
from pylab import *
from aes_base import t_alpha

# SubBytes: calculate (A x message^-1.T) XOR c 
# Param: message = nx4x4 array
# Return: tab_b: message after transformation
def subBytes(m):

	A_SIZE = 8
	M_SIZE = 4

	# Test the array's size for the m parameter
	if (len(m[0]) != len(m[1]) and len(m[1]) != len(m[2]) and len(m[2]) != len(m[3]) and len(m[3]) != M_SIZE):
		raise ValueError("Bad message size in subBytes")

	# Array A (binary 8x8)
	tab_A = [
	[1,0,0,0,1,1,1,1],
	[1,1,0,0,0,1,1,1],
	[1,1,1,0,0,0,1,1],
	[1,1,1,1,0,0,0,1],
	[1,1,1,1,1,0,0,0],
	[0,1,1,1,1,1,0,0],
	[0,0,1,1,1,1,1,0],
	[0,0,0,1,1,1,1,1]]

	# Array m after subBytes transformation
	tab_b = [[ 0 for line in range(M_SIZE)] for col in range(M_SIZE)]

	# Vector C
	tab_c = [1,1,0,0,0,1,1,0]

	# For each message's case
	for cpt_l in range(M_SIZE):
		for cpt_c in range(M_SIZE):
			# Multiplication - change to binary: '{0:08b}'.format(nb)
			b = dot(tab_A, array(list(map(int, bin(int(aes_base.inverseGF(str(m[cpt_l][cpt_c]))))[2:].zfill(8)))).T) %2
			
			# XOR
			b ^= tab_c
			# Convert back to decimal
			result = ''
			for i in range(A_SIZE):
				result += str(b[i])
			result = int(result, 2)
			# Putting
			tab_b[cpt_l][cpt_c] = result

	return(tab_b)


# InvSubByes: calculate (A x message.T XOR c)^-1 
# Param: message = nx4x4 array
# Return: tab_b: message after transformation
def invSubBytes(m):

	A_SIZE = 8
	M_SIZE = 4

	# Test the array's size for the m parameter
	if (len(m[0]) != len(m[1]) and len(m[1]) != len(m[2]) and len(m[2]) != len(m[3]) and len(m[3]) != M_SIZE):
		raise ValueError("Bad message size in invSubBytes")
	
	# Array A (binary 8x8)
	tab_A = [
	[0,0,1,0,0,1,0,1],
	[1,0,0,1,0,0,1,0],
	[0,1,0,0,1,0,0,1],
	[1,0,1,0,0,1,0,0],
	[0,1,0,1,0,0,1,0],
	[0,0,1,0,1,0,0,1],
	[1,0,0,1,0,1,0,0],
	[0,1,0,0,1,0,1,0]]

	# Array m after subBytes transformation
	tab_b = [[ 0 for col in range(M_SIZE)] for cpt in range(M_SIZE)]

	# Vector C
	tab_c = [1,0,1,0,0,0,0,0]

	# For each message's case
	for cpt_l in range(M_SIZE):
		for cpt_c in range(M_SIZE):				
			# Multiplication - change to binary: '{0:08b}'.format(nb)
			b = dot(tab_A, array(list(map(int,bin(m[cpt_l][cpt_c])[2:].zfill(8)))).T) %2

			# XOR
			b ^= tab_c
			# Convert back to decimal
			result = ''
			for i in range(A_SIZE):
				result += str(b[i])

			# Inverse
			result = int(aes_base.inverseGF(aes_base.bin2dec(result)))

			# Putting
			tab_b[cpt_l][cpt_c] = result

	return(tab_b)

