#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    new_string = ""
    for char in my_string:
        if char != "c" or char != "C":
            new_string = new_string + char
    return(new_string)
