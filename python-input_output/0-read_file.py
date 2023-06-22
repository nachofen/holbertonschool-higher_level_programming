#!/usr/bin/python3
"""Task 0- Read file."""


def read_file(filename=""):
    """reads a text file using UTF8 and prints it to stdout"""
    with open(filename, encoding="utf-8") as file:
        text = file.read()
        print(text, end="")
