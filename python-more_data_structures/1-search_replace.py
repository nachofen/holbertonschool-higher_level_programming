#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list2 = list(my_list)
    for number in range(len(my_list2)):
        if my_list2[number] == search:
            my_list2[number] = replace
    return my_list2
