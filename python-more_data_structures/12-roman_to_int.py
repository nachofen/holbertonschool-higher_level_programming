#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or (not isinstance(roman_string, str)):
        return 0
    number_list = []
    result = 0
    for number in roman_string:
        if number == "I":
            number_list.append(1)
        elif number == "V":
            number_list.append(5)
        elif number == "X":
            number_list.append(10)
        elif number == "L":
            number_list.append(50)
        elif number == "C":
            number_list.append(100)
        elif number == "D":
            number_list.append(500)
        elif number == "M":
            number_list.append(1000)
    for final_number in number_list:
        if result < final_number:
            result = final_number - result
        else:
            result = result + final_number
    return result
