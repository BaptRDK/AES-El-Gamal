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
    quotient = round(fileSize / 16 )
    reste = (fileSize % 16 )
    nbArr = quotient + reste

    tabMess = [nbArr * [[4 * [0] , 4 * [0]]]]

    bourrage = 16 - reste
    for i in range(round($

    l = reste
    for i in range(1, quotient + 1 ):
        for j in range(0, 4):
            for k in range(0, 4):
                tabMess[i][j][k] = byteArr[l]
                l = l + 1
