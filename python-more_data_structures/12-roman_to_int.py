#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or (not isinstance(roman_string, str)):
        return 0
    rom_val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    result = 0
    for i in range(len(roman_string)):
        if roman_string[i] not in rom_val:
            return 0
        elif (i < (len(roman_string) - 1) and
                rom_val[roman_string[i]] < rom_val[roman_string[i + 1]]):
            result -= rom_val[roman_string[i]]
        else:
            result = result + rom_val[roman_string[i]]
    return result
