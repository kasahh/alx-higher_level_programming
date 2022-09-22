#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    arr = sys.argv
    larr = len(sys.argv)

    if larr != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if arr[2] != "+" and arr[2] != "-" and arr[2] != "*" and arr[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(arr[1])
    b = int(arr[3])
    op = arr[2]

    if op == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    main()
