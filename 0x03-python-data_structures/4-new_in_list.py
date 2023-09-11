#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        newL = my_list[:]
        newL[idx] = element
        return (newL)
    else:
        return (my_list)
