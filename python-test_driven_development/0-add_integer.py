#!/usr/bin/python3
"""
add intenger function
"""
def add_integer(a, b=98):
    if not isinstance (a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        int(a)
    elif isinstance(b, float):
        int(b)
    return int((a + b))