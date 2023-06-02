#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_num = len(sys.argv) - 1
    arg_list = sys.argv[1:]  # this will exclude argv[0]
    if arg_num == 1:
        print("{} argument:".format(arg_num))
        print("{}: {}".format(arg_num, arg_list[0]))

    elif arg_num == 0:
        print("{} arguments.".format(arg_num))
    else:
        print("{} arguments:".format(arg_num))
        for i in range(1, arg_num + 1):
            print("{}: {}".format(i, arg_list[i - 1]))
