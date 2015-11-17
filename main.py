#! /usr/bin/python3.4
import sys
import segmess
import shiftRows
import addRoundKey

try:
#print segmess.segmess(sys.argv[1])

#tab = [range(4)] * 4

#tab2 = shiftRows.shiftRows(tab, 256)
#print(tab)

#tab3 = shiftRows.invShiftRows(tab, 256)
#print(tab3)

    tab = [[255]*4]*4
    key = [[0]*4]*4

    print(tab)

    print(key)


    tab2 = addRoundKey.addRoundKey(tab, tab)
    print(tab2)
except ValueError as err:
    print(str(err))
