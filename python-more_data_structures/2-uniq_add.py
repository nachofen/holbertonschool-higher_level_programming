#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    result = 0
    for numbers in range(len(my_list)):
        if my_list[numbers] != my_list[numbers - 1]:
            result = result + my_list[numbers]
    return(result)
