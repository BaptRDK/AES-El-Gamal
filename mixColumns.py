#! /usr/bin/python3.4

# MixColumns Function

from pylab import *

def mixColumns(m):
	
	M_SIZE = 4
	tab_a = [0 for row in range(M_SIZE)]	
	tab_b = [0 for row in range(M_SIZE)]	

	c = 0
	h = 0

	for cpt_l in range(M_SIZE):
		tab_a[c] = m[c]
		
