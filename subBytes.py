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

	# Array A (decimal)
	tab_A = [
	[143],
	[199],
	[227],
	[241],
	[248],
	[124],
	[62],
	[31]]

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
	tab_b = [[[0 for row in range(M_SIZE)] for col in range(M_SIZE)] for cpt in range(len(m))]

	# Vector C
	tab_c = [1,1,0,0,0,1,1,0]

	# DEBUG
	#print(len(m))
	print("Message avant modifications:")
	print(m)

	# For each message's case
	for cpt_l in range(len(m)):
		for cpt_c in range(M_SIZE):
			for cpt in range(M_SIZE):
				# Multiplication - change to binary: '{0:08b}'.format(nb)
				#b = dot(tab_A, array(list(map(int,bin(m[cpt_l][cpt_c][cpt])[2:].zfill(8))))).T) % 2
				
				# DEBUG:
				# print(m[cpt_l][cpt_c][cpt])
				# b = dot(tab_A, array(list(map(int,bin(85)[2:].zfill(8)))).T) %2
				b = dot(tab_A, array(list(map(int,bin(m[cpt_l][cpt_c][cpt])[2:].zfill(8)))).T) %2
				
				# XOR
				b ^= tab_c
				# Convert back to decimal
				result = ''
				for i in range(A_SIZE):
					result += str(b[i])
				result = int(result, 2)
				# Putting
				tab_b[cpt_l][cpt_c][cpt] = result

	# DEBUG:
	print("Messages après modifications:")
	print(tab_b)

	return(tab_b)

