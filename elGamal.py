from random import randrange
import rabinMiller

'''
#calculate a generator for Z/Zn
def calgene(n):
    clef = int(n)
    result = [0] * clef
    tmp =-1

    for i in range(2, clef):
        j=1
        k=1
        while j <= (clef-1):
            tmp = i**j % clef
            if result[tmp] == 0:
                result[tmp] = 1

                if tmp == 1:
                    while k <= (clef - 1) and result[k] != 0:
                        k = k+1
                    if k == clef:
                        return(i)
                    k = 1
            j = j+1
        result = [0] * clef
        tmp = -1
'''

#trying the lagrange theoreme
def lagrange(n):
    clef = int(n)
    sousClef = clef - 1
    result = []

    #listing all divisor of sousClef
    for i in range(2, int((sousClef/2)+1)):
        if ((sousClef / i ) % 1) == 0:
            result.append(i)

    result.append(sousClef)

    return(result)

def calcGene(n):
    clef = int(n)
    diviseur = lagrange(clef)
    nbDiviseur = len(diviseur)
    sousClef = clef-1

    for i in range(2, clef):
        j = 0
        while j < nbDiviseur:
            tmp = (i**diviseur[j]) % clef
            
            if tmp == 1:
                if diviseur[j] == sousClef:
                    return(i)
                else:
                    j = nbDiviseur

            j = j+1
#generate and store in a file a 256-bits couple of keys
def keygen():

    tailleClef = 16
    clef = randrange(0, 2**tailleClef)

    while not rabinMiller.isPrime(clef):
        clef = randrange(2, 2**tailleClef)
    
    #write the first part of the public key into a file
    file = open("clefQ", 'w')
    file.write(str(clef))
    file.close()

    #write the second part of the public key into another file
    generator = calcGene(clef)
    file = open("clefP", 'w')
    file.write(str(generator))
    file.close()

    #randomly generate the secret key, it must be <clefQ
    secret = randrange(1, clef)
    file = open("clefS", 'w')
    file.write(str(secret))
    file.close()

    #calculate the third part of the public key and write it into a fourth file
    file = open("clefH", 'w')
    file.write(str((generator**secret)%clef))
    file.close()


