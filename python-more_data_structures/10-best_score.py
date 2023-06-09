#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = 0
    best_key = None
    if isinstance(a_dictionary, dict):
        if len(a_dictionary.items()) > 0:
            for key, value in a_dictionary.items():
                if value >= best_score:
                    best_score = value
                    best_key = key
            return (best_key)
        else:
            return (None)
