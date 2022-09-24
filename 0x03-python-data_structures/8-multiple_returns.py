#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence:
        sentc = [i for i in sentence]
        length = len(sentc)
        first = sentc[0]
        return (length, first)
    else:
        return (0, None)
