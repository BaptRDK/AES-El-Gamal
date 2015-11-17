#! /usr/bin/python3.4
import sys
import segmess
import shiftRows
import matplotlib


#print segmess.segmess(sys.argv[1])

tab = [range(4)] * 4

tab2 = shiftRows.shiftRows(tab, 256)
print(tab)

tab3 = shiftRows.invShiftRows(tab, 256)
print(tab3)
