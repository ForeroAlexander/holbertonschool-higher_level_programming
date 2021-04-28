#!/usr/bin/python3
for abc in range(97, 97 + 26):
    if abc == 113 or abc == 101:
        continue
    print("{:c}".format(abc), end='')
