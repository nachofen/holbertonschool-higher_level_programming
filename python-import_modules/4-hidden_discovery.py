#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)  # saving all names in variable names
    sorted_names = sorted(names)
    for name in names:
        if names[:2] != "__":
            print("{}".format(sorted_names))
