#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0
    arg_num = len(sys.argv) - 1
    arg_list = sys.argv[1:]  # this will exclude argv[0]
    for arg in arg_list:
        res = res + int(arg)
    print("{}".format(res))
