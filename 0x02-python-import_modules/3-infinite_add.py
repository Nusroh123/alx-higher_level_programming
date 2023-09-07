#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    for i, ele in enumerate(sys.argv):
        if i == 0:
            continue
        s = int(ele)
        add += s
    print("{}".format(add))
