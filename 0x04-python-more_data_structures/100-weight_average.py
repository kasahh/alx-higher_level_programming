#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list:
        tup_sum = 0
        av_sum = 0
        for i in my_list:
            tup = i[0] * i[1]
            tup_sum += tup
            av_sum += i[1]
        return tup_sum/av_sum
    else:
        return 0
