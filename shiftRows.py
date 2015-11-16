#! /usr/bin/python2.7


#takes a 4*4 array and a key size (4,6 or 8) and shift the row according to AES standard
def shiftRows(message, keySize):

    #tests if the message is valid (i.e. a 4*4 array)
    if len(message) == 4:
        for i in range(4):
            if len(message[i]) != 4:
                raise ValueError('Bad message size in shiftRows(message, keysize)')
    else:
        raise ValueError('Bad message size in shiftRows(message, keysize)')

    #test if the keysize is valid and initializes the corresponding permutations
    if int(keySize) == 128:
        permut = [0, 1, 2, 3]
    elif keySize == 192:
        permut = [0, 1, 2, 3]
    elif keySize ==  256:
        permut = [0, 1, 3, 4]
    else:
        raise ValueError('Bad key Size in shiftRows(message, keysize)')

    for i in range(4):
        message[i] =  decalage(message[i], permut[i])

    return message

#shift n rows (where n=permut) in message (a 1*4 array)
def decalage(message, permut):
    tmp = [x for x in message]
    tmp2 = [0, 0, 0, 0]
    for i in range(permut):
        for j in range(4):
            tmp2[j] = tmp[(3+j)%4]
        tmp = [x for x in tmp2]

    return tmp


