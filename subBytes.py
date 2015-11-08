#! /usr/bin/python3.4

# First function in AES: SubBytes (substitution)
# Bi,j = SubBytes(Mi,j) = A x Mi,j^-1 XOR c

import sys
import os

M_SIZE = 8

tab_A = [
[1,0,0,0,1,1,1,1],
[1,1,0,0,0,1,1,1],
[1,1,1,0,0,0,1,1],
[1,1,1,1,0,0,0,1],
[1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,0,0],
[0,0,1,1,1,1,1,0],
[0,0,0,1,1,1,1,1]]

tab_c = [1,1,0,0,0,1,1,0]

tab_fic = [
[0,1,0,1,1,1,0,0],
[0,0,0,1,0,1,1,0],
[1,1,1,0,0,1,1,1],
[1,1,1,1,0,0,0,0],
[0,0,0,0,0,1,1,1],
[1,1,0,0,1,1,0,0],
[1,0,1,0,1,1,0,0],
[1,0,1,1,0,0,0,1]]

tab_b = [8 * [8 * [0]]]

# Calculate A x m
for i in range(0, M_SIZE-1) :
	for j in range(0, M_SIZE-1) :
		for k in range(0, M_SIZE-1) :
			tab_b[i][j] = int(tab_b[i][j]) + (int(tab_A[i][k]) * int(tab_fic[k][j]))
			k = k+1 
		j = j+1
	i = i+1

for i in range(0, M_SIZE-1) :
	for j in range(0, M_SIZE-1) :
		tab_b[i][j] = int(tab_b[i][j]) + int(tab_c[i])
		j = j+1
	i = i+1

exit(0)
