#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    letter = chr(i)
    if letter not in ('q', 'e'):
        print("{}".format(letter), end="")
