#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_2 = list(my_list)
    for numbers in range(len(list_2)):
        if list_2[numbers] % 2 == 0:
            list_2[numbers] = True
        else:
            list_2[numbers] = False
    return(list_2)
