from aes_base import sbox
from aes_base import Rcon

# Get a key from user password
def keyExpansion(key, key_size):

        Nb = 4
        if(key_size == 128):
                Nk = 4
                Nr = 10
        elif(key_size == 192):
                Nk = 6
                Nr = 12
        elif(key_size == 256):
                Nk = 8
                Nr = 14
        else:
                raise valueError("keyExpansion: bad key size")

        key = process_key(key, Nk)

        w = []
        for word in key:
                w.append(word[:])
        i = Nk

        while i < Nb * (Nr + 1):
                temp = w[i-1][:]
                if i % Nk == 0:
                        temp = SubWord(RotWord(temp))
                        temp[0] ^= Rcon[(i//Nk)]
                elif Nk > 6 and i % Nk == 4:
                        temp = SubWord(temp)

        for j in range(len(temp)):
                temp[j] ^= w[i-Nk][j]
                w.append(temp[:])
                i += 1

        return w

def SubWord(word):
        return [sbox[byte] for byte in word]

def RotWord(word):
        return word[1:] + word[0:1]

def process_key(key, Nk):
        try:
                key = key.replace(" ", "")
                return [[int(key[i*8+j*2:i*8+j*2+2], 16) for j in range(4)]
                        for i in range(Nk)]
        except:
                print ("Password must be hexadecimal.")
                exit()

