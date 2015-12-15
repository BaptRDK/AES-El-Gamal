#! /usr/bin/python3.4

# MixColumns Function

from pylab import *


def mixColumns(m):

	M_SIZE = 4

	# Test the array's size for the m parameter
        if (len(m[0][0]) != len(m[0][1]) and len(m[0][1]) != len(m[0][2]) and len(m[0][2]) != len(m[0][3]) and len(m[0][3]) != M_SIZE):
                raise ValueError("Bad message size in mixColumns")
	
	n = [word[:] for word in state]

	for cpt in range(len(m)):
		for i in range(M_SIZE):
        		n[i][0] = (gfp2[state[i][0]] ^ gfp3[state[i][1]] ^ state[i][2] ^ state[i][3])
			n[i][1] = (state[i][0] ^ gfp2[state[i][1]] ^ gfp3[state[i][2]] ^ state[i][3])
			n[i][2] = (state[i][0] ^ state[i][1] ^ gfp2[state[i][2]] ^ gfp3[state[i][3]])
			n[i][3] = (gfp3[state[i][0]] ^ state[i][1] ^ state[i][2] ^ gfp2[state[i][3]])		

	return 

def invMixColumns(m):

	M_SIZE = 4

	# Test the array's size for the m parameter
        if (len(m[0][0]) != len(m[0][1]) and len(m[0][1]) != len(m[0][2]) and len(m[0][2]) != len(m[0][3]) and len(m[0][3]) != M_SIZE):
                raise ValueError("Bad message size in invMixColumns")
	
	n = [word[:] for word in state]

	for cpt in range(len(m)):
		for i in range(M_SIZE):
        		n[i][0] = (gfp2[state[i][0]] ^ gfp3[state[i][1]] ^ state[i][2] ^ state[i][3])
			n[i][1] = (state[i][0] ^ gfp2[state[i][1]] ^ gfp3[state[i][2]] ^ state[i][3])
			n[i][2] = (state[i][0] ^ state[i][1] ^ gfp2[state[i][2]] ^ gfp3[state[i][3]])
			n[i][3] = (gfp3[state[i][0]] ^ state[i][1] ^ state[i][2] ^ gfp2[state[i][3]])		

	return
