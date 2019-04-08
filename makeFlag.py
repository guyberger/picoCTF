# This script pads the flag with picoCTF{}

import sys
fout = open("flag.txt", "w+")
if (len(sys.argv) > 1):
    flag = sys.argv[1]
    out = "picoCTF{" + flag + "}"
    fout.write(out)
