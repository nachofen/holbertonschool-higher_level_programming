#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    rev_list = list(reversed(my_list))
    for number in rev_list:
        print("{:d}".format(number))
