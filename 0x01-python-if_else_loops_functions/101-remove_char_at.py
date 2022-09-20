#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = [i for i in str]
    print(newstr)
    del[n]
    print(newstr)
    finstr = ""
    for i in newstr:
        finstr += i
    return finstr

