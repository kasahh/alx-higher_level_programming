#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        score_list = []
        for key in a_dictionary:
            score_list.append(a_dictionary[key])
        score_list.sort()
        best = score_list[-1]
        for key in a_dictionary:
            if a_dictionary[key] == best:
                return key
