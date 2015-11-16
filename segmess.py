#! /usr/bin/python2.7

import sys
import os

#function to segment the message in n 4*4 matrix (each containing 128 bits)
def segmess(message):

    if not os.path.isfile(str(message)):
        print "Le fichier " + message + " n\'existe pas"
        sys.exit(2)
    
    #get the file in binary and map it before closing it
    f = open(str(message), "rb")
    byteArr = map(ord, f.read())
    f.close()

    fileSize = len(byteArr)
    quotient = fileSize / 16
    reste = (fileSize % 16 )

    init = 0
    if reste != 0:
        tabMess = [[[0 for i in range(4)] for i in range(4)] for i in range(quotient+1)]
        bourrage = 16 - reste
        j = 0

        for i in range(bourrage, 16):
            tabMess[0][i/4][i%4] = byteArr[j]
            j = j + 1
        init=1
    else:
        tabMess = [[[0 for i in range(4)] for i in range(4)] for i in range(quotient)]

    l = reste
    for i in range(init, quotient + init):
        for j in range(0, 4):
            for k in range(0, 4):
                tabMess[i][j][k] = byteArr[l]
                l = l + 1
    return tabMess
