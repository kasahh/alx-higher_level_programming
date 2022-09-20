#!/usr/bin/python3
s = 122
for i in range(0,26):
    print("{}".format(chr(s)), end="")
    if i%2 == 0:
        s -= 33
    else:
        s += 31
