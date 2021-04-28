#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    if c % 2 != 0:
        c = c - ord(' ')
    print('{:s}'.format(chr(c)), end='')
