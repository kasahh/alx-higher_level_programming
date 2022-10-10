#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for i in my_list:
            if x > 0:
                print(i, end = '')
                num += 1
                x -= 1
    except Exception:
        pass
    print("\n")
    return num
