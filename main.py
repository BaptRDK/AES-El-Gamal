#! /usr/bin/python3.4
import sys
import aes

try:
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

	print("===========================================================")
	print("==================== PYAES & PEL GAMAL ====================")
	print("===========================================================")
	print("\n")

	print("Please choose one encryption method:")
	print("1- AES: Advanced (symetric) Encryption Standard")
	print("2- El Gamal: Asymetric encryption")
	print("3- El Gamal: File signature")
	algo = input()
	algo = int(algo)
	
	while (algo < 1 or algo > 3):
		print("Please choose one encryption method:")
		print("1- AES: Advanced (symetric) Encryption Standard")
		print("2- El Gamal: Asymetric encryption")
		print("3- El Gamal: File signature")
		algo = input()	
		algo = int(algo)
	print("\n")
	

	# AES
	if (algo == 1):
		print("Please select key size:")
		print("1- 128 bits")
		print("2- 192 bits")
		print("3- 256 bits")
		key = input()
		key = int(key)
		while (key < 1 or key > 3):
			print("Please select key size:")
			print("1- 128 bits")
			print("2- 192 bits")
			print("3- 256 bits")
			key = input()	
			key = int(key)

		if (key == 1):
			key_size = 128
		elif (key == 2):
			key_size = 192
		elif (key == 3):
			key_size = 256

		print("Do you want to crypt or uncrypt?")
		print("1- Crypt")
		print("2- Uncrypt")
		mode = input()
		mode = int(mode)
		while (mode < 1 or mode > 2):
			print("Do you want to crypt or uncrypt?")
			print("1- Crypt")
			print("2- Uncrypt")
			mode = input()
			mode = int(mode)
		
		print("Please give me your filename (must be in the current directory:")
		file = input()

		# while file !exists:
		#	print("Please give me your filename (must be in the current directory:")
		#	file = input()

		print("Please insert your password:")
		pwd = input()

		if (mode == 1):
			aes.crypt(file, key_size, pwd)
		elif (mode == 2):
			aes.uncrypt(file, key_size, pwd)

	# El Gamal encryption


	# El Gamal signature
	elif (algo == 3):
		print("Sorry, this feature is not implemented yet")
 

except ValueError as err:
	print(str(err))
