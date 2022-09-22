#!/usr/bin/python3
import hidden_4


def main():
    arr = dir(hidden_4)

    for i in arr:
        if i[0] == "_" and i[1] == "_":
            pass
        else:
            print(i)


if __name__ == "__main__":
    main()
