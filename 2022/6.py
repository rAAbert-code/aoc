#!/usr/bin/python3

import os
import sys
import re
import copy

def getfilename():
    args = sys.argv
    dir_name = os.path.dirname(args[0])
    file_name = os.path.basename(args[0])[0]
    if len(args) < 2:
        file_name += ".data"
    elif args[1] == "-s":
        file_name += ".sample"
    else:
        sys.exit("Unknown argument")
    return dir_name + "/input/" + file_name

def puzzle(file):
    line = file.readline()
    length = len(line)
    p0, p1 = 0, 3

    while p1 < length:
        s = set(line[p0:p1+1])
        if len(s) == 4:
            # found key
            break
        else:
            p0, p1 = p0+1, p1+1

    print(p1+1)

def main():
    file_name = getfilename()

    with open(file_name, "r") as file:
        puzzle(file)

if __name__ == "__main__":
    main()

