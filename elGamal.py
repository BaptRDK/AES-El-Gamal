from random import randrange
import rabinMiller


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


