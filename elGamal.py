from random import randrange
import rabinMiller


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



#generate and store in a file a 256-bits couple of keys
def keygen(fic):

    tailleClef = 16
    clef = randrange(0, 2**tailleClef)

    while not rabinMiller.isPrime(clef):
        clef = randrange(2, 2**tailleClef)
    
    file = open("clefQ", 'w')
    file.write(str(clef))
