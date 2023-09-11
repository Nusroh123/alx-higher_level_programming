#!/usr/bin/python3
def element_at(my_list, idx):
    listLen = len(my_list)
    if idx < 0:
        return (None)
    currentIndex = 0
    for element in my_list:
        if currentIndex == idx:
            return (element)
        currentIndex += 1

    return (None)
