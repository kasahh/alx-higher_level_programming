#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    loops = new_list.count(search)
    while loops > 0:
        index = new_list.index(search)
        new_list[index] = replace
        loops -= 1
    return new_list
