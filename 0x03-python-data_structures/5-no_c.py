#!/usr/bin/python3


def no_c(my_string):
    new_string = ''
    my_string = [i for i in my_string]
    while 'c' in my_string:
        my_string.remove('c')
    while 'C' in my_string:
        my_string.remove('C')
    for i in my_string:
        new_string += i
    return new_string
