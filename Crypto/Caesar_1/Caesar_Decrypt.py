

# This script decrypts Caesar Cypher, limited for 'a'-'z' (small caps).
# Args: [filename] containing the text to decrypt.
# The output is all 26 possible decryptions.

import sys

def main():
    if(len(sys.argv) < 2):
        print("Need a file as argument")
        return
    try:
        f = open(sys.argv[1], 'r')
        s, pad = "", 0
        secret = f.read()   #contains the new line character at the end
        while(pad < 26):
            for c in secret:
                s += chr((ord(c)-ord('a') + pad)%26 + ord('a'))
            pad += 1
            print(s[:len(s)-1])     #remove nl character
            s = ""
    except IOError:
        print("No file to open")


if __name__ == "__main__":
    main()
