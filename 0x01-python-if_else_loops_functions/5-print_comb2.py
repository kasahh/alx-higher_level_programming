#!/usr/bin/python3
for i in range(0, 100):
    if i < 99:
        end = ", "
    else:
        end = ""
    print("{0:02d}".format(i), end=end)
print("\n")
