from random import randrange
from os import path
import pickle
import rabinMiller
from confElGamal import tailleClef, nomClef


#using the lagrange theoreme, i.e. listing all the possible divisors
def lagrange(n):
    clef = int(n)
    sousClef = clef - 1
    result = []

    #listing all divisor of sousClef
    #for all number below (clef/2)
    for i in range(2, int((sousClef/2)+1)):

        #check if the divides sousClef
        if ((sousClef / i ) % 1) == 0:
            #building a list of all divisors
            result.append(i)

    #adding sousClef as a divisor of sousClef to the list
    result.append(sousClef)

    return(result)

#calculating one generator element for Z/nZ
def calcGene(n):
    clef = int(n)
    #getting the list of divisors for n
    diviseur = lagrange(clef)
    #and the size of this list
    nbDiviseur = len(diviseur)
    sousClef = clef-1

    #for each number between 2 and clef
    for i in range(2, clef):
        j = 0
        
        #do while j doesn't equal the number of divisor (we don't have tested all the divisor for this i)
        while j < nbDiviseur:
            #calculating the order of this i
            tmp = (i**diviseur[j]) % clef
            
            #when we find it's order
            if tmp == 1:
                #we check if it's order is equal to sousClef (i.e. every elements of the group has been generated)
                if diviseur[j] == sousClef:
                    #if so i is a generator
                    return(i)

                #if not we change j to go on with the next i
                else:
                    j = nbDiviseur

            j = j+1

#generate and store in several files the differents component of the keys
def keygen():

    print("Generating keys, this could take a while...")
    clef = randrange(0, 2**tailleClef)

    while not rabinMiller.isPrime(clef):
        clef = randrange(2, 2**tailleClef)
    
    #write the first part of the public key into a file
    file = open(nomClef[0], 'w')
    file.write(str(clef))
    file.close()

    #write the second part of the public key into another file
    generator = calcGene(clef)
    file = open(nomClef[1], 'w')
    file.write(str(generator))
    file.close()

    #randomly generate the secret key, it must be <clefQ
    secret = randrange(1, clef)
    file = open(nomClef[2], 'w')
    file.write(str(secret))
    file.close()

    #calculate the third part of the public key and write it into a fourth file
    file = open(nomClef[3], 'w')
    file.write(str((generator**secret)%clef))
    file.close()

#encrypt the file fic
def chiffreFic(fic):

    cible = str(fic)
    
    #test if the file exists
    if not path.isfile(cible):
        raise ValueError("ElGamal: invalid entry file")
    
    #test if the pubic key exists
    if not path.isfile(nomClef[3]) or not path.isfile(nomClef[0]) or not path.isfile(nomClef[1]):
        rep = input("Keys not found, do you wish to generate them ?")
        rep = rep.lower()
        
        #if not we can generate it
        if rep == "y" or rep == "o":
            keygen()
        else:
            raise ValueError("ElGamal: Keys not found")

    #opening and storing the 3 components of the public key
    f = open(nomClef[0], "r")
    clefQ = int(f.read())
    f.close()

    f = open(nomClef[3], "r")
    clefH = int(f.read())
    f.close()
    
    f = open(nomClef[1], "r")
    clefG = int(f.read())
    f.close()

    #get the file in binary and map it before closing it
    f = open(cible, "rb")
    byteArr = list(f.read())
    f.close()
    
    c1c2 = [] 
    
    #encrypting each byte of the file
    for byte in byteArr:
        #random Y for each byte(block)
        clefY = randrange(1, clefQ)
        #first we happen c1
        c1c2.append((clefG**clefY) % clefQ)

        secret = (clefH**clefY) % clefQ
        
        #then c2
        c1c2.append((byte*secret))
    
    
    result = cible + ".chif"
    
    #creating the encrypted file
    f = open(result, "wb")
    pickle.dump(c1c2, f)

#decrypting function
def deChiffreFic(fic):
    cible = str(fic)
    result = cible + ".clr"

    #test if the file exists
    if not path.isfile(cible):
        raise ValueError("ElGamal: invalid entry file")

    #test if the pubic key exists
    if not path.isfile(nomClef[0]) or not path.isfile(nomClef[2]):
        raise ValueError("ElGamal: secret key not found")

    #opening and storing the public key
    f = open(nomClef[2], "r")
    secret = int(f.read())
    f.close()

    f = open(nomClef[0], "r")
    clefQ = int(f.read())
    f.close()

    f = open(cible, "rb")
    crypt = pickle.load(f)
    f.close()

    i = 0
    clair = [] 

    
    while i < len(crypt):
        #decrypting
        clair.append(int(crypt[i+1]/((crypt[i]**secret)%clefQ)))
        i = i + 2

    #opening a new file for the decrypted file
    f = open(result, "wb")
    f.write(bytes(clair))
    f.close()





    
