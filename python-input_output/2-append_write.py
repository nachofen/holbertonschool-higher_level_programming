#!/usr/bin/python3
"""Task 2- append to a file."""


def append_write(filename="", text=""):
    """appends a string to the end of a text file with utf8 and returns number
    of chars added"""
    added_chars = 0
    for chars in (text):
        added_chars += 1
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return (added_chars)
