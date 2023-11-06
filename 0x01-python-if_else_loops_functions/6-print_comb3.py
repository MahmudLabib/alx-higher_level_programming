#!/usr/bin/python3
# Auther - Mahmud labib

for i in range(0, 10):
    for j in range(i, 10):
        if i == j:
            continue
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=', ')
