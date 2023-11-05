#!/usr/bin/python3
for number in range(ord("a"), ord("z") + 1):
    if number == ord("q") or number == ord("e"):
        continue
    print("{}".format(chr(number)), end='')
