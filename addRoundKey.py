#addRoundKey function of the AES standard, xor the state (message: 4*4 array)  with a sub-key (key: 4*4 array)
def addRoundKey(message, key):
    #tests if the message is valid (i.e. a 4*4 array) and if the key is valid (same condition)
    if len(message) == 4 or len(key):
        for i in range(4):
            if len(message[i]) != 4 or len(key[i]) != 4:
                raise ValueError('Bad message size in addRoundKey(message, key)')
    
    else:
        raise ValueError('Bad message size in addRoundKey(message, key)')
    
    tmp = [[0 for x in range(4)] for x in range(4)]

    #xor each octet o th message with its corresponding octet in the subkey
    for i in range(4):
        for j in range(4):
            tmp[i][j] = message[i][j] ^ key[i][j]

    return tmp

