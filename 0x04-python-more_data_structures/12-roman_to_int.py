#!/usr/bin/python3
def roman_to_int(roman_string):
    romanToInt = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
    total = 0
    prevRoman = 0

    if type(roman_string) is not str or None:
        return (0)

    for number in reversed(roman_string):
        roman = romanToInt[number]
        if roman < prevRoman:
            total -= roman
        else:
            total += roman

        prevRoman = roman

    return (total)
