#!/usr/bin/python3
import sys


def main():
    arr = sys.argv
    larr = len(sys.argv)
    sum = 0

    if larr <= 1:
        print(sum)
    else:
        for i in arr:
            if i != arr[0]:
                sum += int(i)
        print(sum)


if __name__ == "__main__":
    main()
