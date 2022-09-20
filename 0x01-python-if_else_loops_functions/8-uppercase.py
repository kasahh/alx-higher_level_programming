#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        y = ord(str[i])
        if (y >= 97) and (y <= 122):
            y -= 32
            # str = str.replace(str[i],chr(y))
            str = "{}".format(str.replace(str[i],chr(y)))
    
    print("{}".format(str))
    return str
