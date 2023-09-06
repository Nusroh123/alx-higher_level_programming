#!/usr/bin/python3
def uppercase(str):
    upperCase = ""
    for char in str:
        if 'a' <= char <= 'z':
            upperCase += chr(ord(char) - 32)
        else:
            upperCase += char
    print("{}".format(upperCase))
