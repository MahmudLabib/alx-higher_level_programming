#!/usr/bin/python3
def no_c(my_string):
    table = {67 : None, 99 : None}
    my_string = my_string.translate(table)
    return my_string
