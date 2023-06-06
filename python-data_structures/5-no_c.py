#!/usr/bin/python3
def no_c(my_string):
    if isinstance(my_string, str):
        new_string = ""
        for char in my_string:
            if char != "c"  and char != "C":
                new_string = new_string + char
        return(new_string)
