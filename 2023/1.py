#!/usr/bin/python3
#jdfjkdsf

import os
import sys
import re
import copy

def p1(lines):
    sum = 0

    for line in lines:
        first = last = -1
        for index, char in enumerate(line):
            if char.isdigit():
                if first == -1:
                    first = int(char) 
                last = int(char)
        number = first*10 + last
        sum += number
    return(sum)

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def p2(lines):
    sum = 0

    for line in lines:
        length = len(line)
        first = last = -1
        index = 0

        print(line)

        while index < length:
            digit = -1
            #print(index)

            #print("looking for integer")
            c = line[index]
            if c.isdigit():
                digit = int(c)
                print("Found", digit, "at index", index)
            else:
                #print("looking for text")
                for i, number in enumerate(numbers):
                    if line[index:].find(number) == 0:
                        digit = i
                        print("Found", number, digit, "at index", index)
                        break

            index += 1

            if digit == -1:
                #print("Didn't find a digit")
                continue

            # We found a digit
            if first == -1:
                first = digit
            last = digit

        number = first*10 + last
        print(first, last, number, "\n")
        sum += number
    return(sum)

               

    return(sum)
