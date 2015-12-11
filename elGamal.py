from random import randrange
import rabinMiller

#generate and store in a file a 256-bits couple of keys
def keygen(fic):

    tailleClef = 32
    clef = randrange(0, 2**tailleClef)

    while not rabinMiller.isPrime(clef):
        clef = randrange(2, 2**tailleClef)
    return clef
