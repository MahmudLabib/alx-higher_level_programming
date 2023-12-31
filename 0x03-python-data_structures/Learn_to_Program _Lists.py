#!/usr/bin/python3

# ---------- LEARN TO PROGRAM 6 ----------

import random
import math

# With lists we can refer to groups of data with 1 name

# Each item in the list corresponds to a number (index)
# just like how people have identification numbers.
# By default the 1st item in a list has the index 0

# [0 : "string"] [1 : 1.234] [2 : 28] [3 : "c"]

# Python lists can grow in size and can contain data
# of any type

randList = ["string", 1.234, 28]

# Create a list with range
oneToTen = list(range(10))

# An awesome thing about lists is that you can use many
# of the same functions with them that you used with strings

# Combine lists
randList = randList + oneToTen

# Get the 1st item with an index
print(randList[0])

# Get the length
print("List Length :", len(randList))

# Slice a list to get 1st 3 items
first3 = randList[0:3]

# Cycle through the list and print the index
for i in first3:
    print("{} : {}".format(first3.index(i), i))

# You can repeat a list item with *
print(first3[0] * 3)

# You can see if a list contains an item
print("string" in first3)

# You can get the index of a matching item
print("Index of string :", first3.index("string"))

# Find out how many times an item is in the list
print("How many strings :", first3.count("string"))

# You can change a list item
first3[0] = "New String"

for i in first3:
    print("{} : {}".format(first3.index(i), i))

# Append a value to the end of a list
first3.append("Another")

# ---------- PROBLEM : CREATE A RANDOM LIST ----------
# Generate a random list of 5 values between 1 and 9
numList = []
for i in range(5):
    numList.append(random.randrange(1, 9))

# ---------- SORT A LIST : BUBBLE SORT ----------
# The Bubble sort is a way to sort a list
# It works this way
# 1. An outer loop decreases in size each time
# 2. The goal is to have the largest number at the end of
#    the list when the outer loop completes 1 cycle
# 3. The inner loop starts comparing indexes at the beginning
#    of the loop
# 4. Check if list[Index] > list[Index + 1]
# 5. If so swap the index values
# 6. When the inner loop completes the largest number is at
#    the end of the list
# 7. Decrement the outer loop by 1

# Create the value that will decrement for the outer loop
# Its value is the last index in the list
i = len(numList) - 1

while i > 1:

    j = 0

    while j < i:

        # Tracks the comparison of index values
        print("\nIs {} > {}".format(numList[j], numList[j+1]))
        print()

        # If the value on the left is bigger switch values
        if numList[j] > numList[j+1]:

            print("Switch")

            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp

        else:
            print("Don't Switch")

        j += 1

        # Track changes to the list
        for k in numList:
            print(k, end=", ")
        print()

    print("END OF ROUND")

    i -= 1

for k in numList:
    print(k, end=", ")
print()

# ---------- MORE LIST FUNCTIONS ----------
numList = []
for i in range(5):
    numList.append(random.randrange(1, 9))

# Sort a list
numList.sort()

# Reverse a list
numList.reverse()

for k in numList:
    print(k, end=", ")
print()

# Insert value at index insert(index, value)
numList.insert(5, 10)

# Delete first occurrence of value
numList.remove(10)

for k in numList:
    print(k, end=", ")
print()

# Remove item at index
numList.pop(2)

for k in numList:
    print(k, end=", ")
print()

# ---------- LIST COMPREHENSIONS ----------
# You can construct lists in interesting ways using
# list comprehensions

# Perform an operation on each item in the list

# Create a list of even values
evenList = [i*2 for i in range(10)]

for k in evenList:
    print(k, end=", ")
print()

# List of lists containing values to the power of
# 2, 3, 4
numList = [1,2,3,4,5]

listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]
                for m in numList]

for k in listOfValues:
    print(k)
print()

# Create a 10 x 10 list
multiDList = [[0] * 10 for i in range(10)]

# Change a value in the multidimensional list
multiDList[0][1] = 10

# Get the 2nd item in the 1st list
# It may help to think of it as the 2nd item in the 1st row
print(multiDList[0][1])

# Get the 2nd item in the 2nd list
print(multiDList[1][1])

# ---------- MULTIDIMENSIONAL LIST ----------

# Show how indexes work with a multidimensional list
listTable = [[0] * 10 for i in range(10)]

for i in range(10):

    for j in range(10):
        listTable[i][j] = "{} : {}".format(i, j)

for i in range(10):

    for j in range(10):
        print(listTable[i][j], end=" || ")
    print()

# ---------- PROBLEM : CREATE MULTIPLICATION TABLE ----------
# With 2 for loops fill the cells in a multidimensional
# list with a multiplication table using values 1 - 9
'''
1, 2, 3, 4, 5, 6, 7, 8, 9,
2, 4, 6, 8, 10, 12, 14, 16, 18,
3, 6, 9, 12, 15, 18, 21, 24, 27,
4, 8, 12, 16, 20, 24, 28, 32, 36,
5, 10, 15, 20, 25, 30, 35, 40, 45,
6, 12, 18, 24, 30, 36, 42, 48, 54,
7, 14, 21, 28, 35, 42, 49, 56, 63,
8, 16, 24, 32, 40, 48, 56, 64, 72,
9, 18, 27, 36, 45, 54, 63, 72, 81
'''

# Create the multidimensional list
multTable = [[0] * 10 for i in range(10)]

# This will increment for each row
for i in range(1, 10):

    # This will increment for each item in the row
    for j in range(1, 10):

        # Assign the value to the cell
        multTable[i][j] = i * j

# Output the data in the same way you assigned it
for i in range(1, 10):

    for j in range(1, 10):
        print(multTable[i][j], end=", ")

    print()
