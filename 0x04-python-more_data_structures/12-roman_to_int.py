#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    if roman_string:
        value_list = []
        value = 0
        skip = False
        az = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in roman_string:
            if i in az:
                value_list.append(az[i])
        value_list.reverse()
        size = len(value_list)
        for i in range(size):
            if skip is False:
                if i + 1 < size:
                    if value_list[i] > value_list[i + 1]:
                        m_sum = value_list[i] - value_list[i + 1]
                        value += m_sum
                        skip = True
                    else:
                        value += value_list[i]
                else:
                    value += value_list[i]
            else:
                skip = False
                pass
        return value
    return 0
