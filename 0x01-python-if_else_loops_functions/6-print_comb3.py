#!/usr/bin/python3
for num in range(0, 10):
    for num2 in range(0, 10):
        if num is 8 and num2 is 9:
            print("{:d}{:d}".format(num, num2))
        elif num < num2:
            print("{:d}{:d}".format(num, num2), end=", ")
