#!/usr/bin/python3
def no_c(my_string):
    strToRemove = "cC"
    result = ''.join([char for char in my_string if char not in strToRemove])
    return (result)
