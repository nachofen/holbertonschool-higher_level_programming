#!/usr/bin/python3
"""define mylist class."""


class MyList(list):
    """Define a MyList."""

    def print_sorted(self):
        """print a list sorted in ascending order"""
        print(sorted(self))
