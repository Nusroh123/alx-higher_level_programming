#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argCount = len(sys.argv)
    if argCount == 1:
        print("{} arguments.".format(argCount - 1))
    elif argCount == 2:
        print("{} argument:".format(argCount - 1))
    else:
        print("{} arguments:".format(argCount - 1))
    if argCount > 1:
        for i in range(argCount - 1):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
