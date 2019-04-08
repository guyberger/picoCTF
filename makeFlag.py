# This script pads the flag with picoCTF{}

import sys
fout = open("flag.txt", "w+")
if (len(sys.argv) = 2):
    flag = sys.argv[1]
    out = "picoCTF{" + flag + "}"
    fout.write(out)

else:
    print ("Format: python makeFlag.py FLAG")
