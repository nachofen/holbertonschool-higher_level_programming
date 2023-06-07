#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_2 = dict()
    for key, value in a_dictionary.items():
        dict_2[key] = value * 2
    return (dict_2)
