#! /usr/bin/python3.4

# First function in AES: SubBytes (substitution)
# Bi,j = SubBytes(Mi,j) = A x Mi,j^-1 XOR c

# Array manipulation
from pylab import *

# SubByes: calculate (A x message) + c 
# Param: message = 4x4 array
# Return: tab_b: message after transformation
def subBytes(m):

	A_SIZE = 8
	M_SIZE = 4

	# Test the array's size for the m parameter
	if (len(m[0]) != len(m[1]) and len(m[1]) != len(m[2]) and len(m[2]) != len(m[3]) and len(m[3]) != M_SIZE):
		raise ValueError("Bad message size in subBytes")

	# Array A
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
	tab_b = [[0 for row in range(M_SIZE)] for col in range(M_SIZE)]

	# Vector C
	tab_c = [1,1,0,0,0,1,1,0]

	# For each message's case
	for cpt_l in range(M_SIZE):
		for cpt_c in range(M_SIZE):

			# Multiplication
			b = dot(tab_A, m[cpt_l][cpt_c])
			# XOR
			b ^= tab_c
			# Putting
			tab_b[cpt_l][cpt_c] = b

	return(tab_b)
