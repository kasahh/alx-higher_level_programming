#!/usr/bin/python3
import sys


def main():
    args = sys.argv
    larr = len(sys.argv)
    ind = larr - 1

    if larr <= 1:
        print("0 arguments.")
    elif larr == 2:
        print("1 argument:")
        print("{}: {}".format(ind, sys.argv[ind]))
    else:
        print("{} arguments:".format(ind))
        for i in range(larr):
            if i != 0:
                print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
