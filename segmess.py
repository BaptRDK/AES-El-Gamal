
import sys
import os
from math import floor


#function to segment the message in n 4*4 matrix (each containing 128 bits)
def segmess(message):

    #test if the file exists and, if not, exits
    if not os.path.isfile(str(message)):
        raise ValueError("the file  " + str(message) + " does not exist")
    
    #get the file in binary and map it before closing it
    f = open(str(message), "rb")
    #byteArr = list(map(ord, f.read()))
    byteArr = list(f.read())
    f.close()

    fileSize = len(byteArr)
    quotient = floor(fileSize / 16)
    reste = (fileSize % 16 )

    init = 0
    #if the size of the file is not a factor of 16 we fill the array with 0s to make it
    if reste != 0:
        #creates a array of 4*4 arrays big enough to contains the file
        tabMess = [[[0 for i in range(4)] for i in range(4)] for i in range(quotient+1)]
        bourrage = 16 - reste
        j = 0
        
        #fills the first array with enough 0s to make the final array a 16 factor
        for i in range(bourrage, 16):
            tabMess[0][floor(i/4)][i%4] = byteArr[j]
            j = j + 1
        init=1
    else:
        #If it is already a 16 factor creates a quotient*4*4 array
        tabMess = [[[0 for i in range(4)] for i in range(4)] for i in range(quotient)]

    l = reste
    #fill the array with (the rest of) the file
    for i in range(init, quotient + init):
        for j in range(0, 4):
            for k in range(0, 4):
                tabMess[i][j][k] = byteArr[l]
                l = l + 1
    #return the file formated as n*4*4 array of bytes
    return tabMess
