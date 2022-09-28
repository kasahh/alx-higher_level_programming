#!/usr/bin/python3


def uniq_add(my_list=[]):
    sum = 0
    new_list = my_list.copy()
    new_list = set(new_list)
    for x in new_list:
        sum += x
    return sum
