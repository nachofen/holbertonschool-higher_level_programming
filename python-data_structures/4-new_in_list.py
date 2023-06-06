#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None
    cpy_list = list(my_list)
    if idx < 0 or idx >= len(cpy_list):
        return cpy_list
    cpy_list[idx] = element
    return cpy_list
