
import sys

if len(sys.argv) < 2:
    print("Give me an argument")

elif len(sys.argv) == 2:
    s = ""
    for i in range(int(sys.argv[1])):
        s += 'a'
    print(s)
