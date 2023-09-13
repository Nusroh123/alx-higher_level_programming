#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedDi = sorted(a_dictionary.keys())
    for key in sortedDi:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
