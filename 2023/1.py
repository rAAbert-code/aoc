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


def p2(lines):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    sum = 0

    for line in lines:
        digits = []

        for index, char in enumerate(line):
            if char.isdigit():
                digits.append(char)
            else:
                for i, number in enumerate(numbers):
                    if line[index:].find(number) == 0:
                        digits.append(i)
                        break
        number = int(digits[0])*10 + int(digits[-1])
        sum += number
    return(sum)
