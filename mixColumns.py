#! /usr/bin/python3.4

# MixColumns Function

from pylab import *
from aes_base import sbox, isbox, gfp2, gfp3, gfp9, gfp11, gfp13, gfp14, Rcon

def mixColumns(state):

	M_SIZE = 4

	# Test the array's size for the m parameter
	if (len(state[0][0]) != len(state[0][1]) and len(state[0][1]) != len(state[0][2]) and len(state[0][2]) != len(state[0][3]) and len(state[0][3]) != M_SIZE):
		raise ValueError("Bad message size in mixColumns")
	
	for cpt in range(len(state)):
		n = [word[:] for word in state[cpt]]
		for i in range(M_SIZE):
			n[i][0] = (gfp2[state[cpt][i][0]] ^ gfp3[state[cpt][i][1]] ^ state[cpt][i][2] ^ state[cpt][i][3])
			n[i][1] = (state[cpt][i][0] ^ gfp2[state[cpt][i][1]] ^ gfp3[state[cpt][i][2]] ^ state[cpt][i][3])
			n[i][2] = (state[cpt][i][0] ^ state[cpt][i][1] ^ gfp2[state[cpt][i][2]] ^ gfp3[state[cpt][i][3]])
			n[i][3] = (gfp3[state[cpt][i][0]] ^ state[cpt][i][1] ^ state[cpt][i][2] ^ gfp2[state[cpt][i][3]])		

	return n

def invMixColumns(state):

	M_SIZE = 4

	# Test the array's size for the m parameter
	if (len(state[0][0]) != len(state[0][1]) and len(state[0][1]) != len(state[0][2]) and len(state[0][2]) != len(state[0][3]) and len(state[0][3]) != M_SIZE):
		raise ValueError("Bad message size in invMixColumns")
	
	for cpt in range(len(state)):
		n = [word[:] for word in state[cpt]]
		for i in range(M_SIZE):
			n[i][0] = (gfp2[state[cpt][i][0]] ^ gfp3[state[cpt][i][1]] ^ state[cpt][i][2] ^ state[cpt][i][3])
			n[i][1] = (state[cpt][i][0] ^ gfp2[state[cpt][i][1]] ^ gfp3[state[cpt][i][2]] ^ state[cpt][i][3])
			n[i][2] = (state[cpt][i][0] ^ state[cpt][i][1] ^ gfp2[state[cpt][i][2]] ^ gfp3[state[cpt][i][3]])
			n[i][3] = (gfp3[state[cpt][i][0]] ^ state[cpt][i][1] ^ state[cpt][i][2] ^ gfp2[state[cpt][i][3]])	

	return n
