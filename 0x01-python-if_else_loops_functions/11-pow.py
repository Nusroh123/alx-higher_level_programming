#!/usr/bin/python3
def pow(a, b):
    res = 1
    if b >= 0:
        for i in range(b):
            res *= a
    else:
        b *= -1
        for i in range(b):
            res *= 1 / a
    return (res)
