#!/usr/bin/python3
"""Task 1- Write to a file."""


def write_file(filename="", text=""):
    """writes a string to a text file with utf8 and returns number
    of chars printed"""
    count_chars = 0
    for count_chars in range(len(text)):
        count_chars += 1
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return (count_chars)
