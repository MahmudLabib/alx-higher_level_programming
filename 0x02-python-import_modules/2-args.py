#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ln = len(argv) - 1
    if ln == 0:
        print("{} arguments.".format(ln))
    elif ln > 0:
        print("{} argument:".format(ln))
        for index, value in enumerate(argv):
            if index != 0:
                print("{} {}".format(index, value))
