#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for numbers in (set(my_list)):
        result = result + numbers
    return(result)
