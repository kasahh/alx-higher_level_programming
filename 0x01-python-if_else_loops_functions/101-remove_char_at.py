#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = [i for i in str]
    if n < len(newstr) and n > 0:
        del newstr[n]
    finstr = ""
    for i in newstr:
        finstr += i
    return finstr
