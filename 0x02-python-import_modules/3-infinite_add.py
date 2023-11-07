#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
# argv[] = [1, 2, 3, 4]
    ln = len(argv) - 1
    sum = 0
    if ln == 0:
        print("{}".format(0))
    elif ln > 0:
        for index, value in enumerate(argv):
            if index != 0:
                sum += int(value)
        print("{}".format(sum))
