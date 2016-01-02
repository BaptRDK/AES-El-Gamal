#! /usr/bin/python3.4

# MixColumns Function

from pylab import *
from aes_base import sbox, isbox, gfp2, gfp3, gfp9, gfp11, gfp13, gfp14, Rcon

def mixColumns(state):

	M_SIZE = 4

	# Test the array's size for the m parameter
	if (len(state[0]) != len(state[1]) and len(state[1]) != len(state[2]) and len(state[2]) != len(state[3]) and len(state[3]) != M_SIZE):
		raise ValueError("Bad message size in mixColumns")
	
	n = [word[:] for word in state]
	for i in range(M_SIZE):
		n[i][0] = (gfp2[state[i][0]] ^ gfp3[state[i][1]] ^ state[i][2] ^ state[i][3])
		n[i][1] = (state[i][0] ^ gfp2[state[i][1]] ^ gfp3[state[i][2]] ^ state[i][3])
		n[i][2] = (state[i][0] ^ state[i][1] ^ gfp2[state[i][2]] ^ gfp3[state[i][3]])
		n[i][3] = (gfp3[state[i][0]] ^ state[i][1] ^ state[i][2] ^ gfp2[state[i][3]])
	return n

def invMixColumns(state):

	M_SIZE = 4

	# Test the array's size for the m parameter
	if (len(state[0]) != len(state[1]) and len(state[1]) != len(state[2]) and len(state[2]) != len(state[3]) and len(state[3]) != M_SIZE):
		raise ValueError("Bad message size in invMixColumns")
	
	n = [word[:] for word in state]
	for i in range(M_SIZE):
		n[i][0] = (gfp14[state[i][0]] ^ gfp11[state[i][1]] ^ gfp13[state[i][2]] ^ gfp9[state[i][3]])
		n[i][1] = (gfp9[state[i][0]] ^ gfp14[state[i][1]] ^ gfp11[state[i][2]] ^ gfp13[state[i][3]])
		n[i][2] = (gfp13[state[i][0]] ^ gfp9[state[i][1]] ^ gfp14[state[i][2]] ^ gfp11[state[i][3]])
		n[i][3] = (gfp11[state[i][0]] ^ gfp13[state[i][1]] ^ gfp9[state[i][2]] ^ gfp14[state[i][3]])

	return n
