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

def find_key(line, kl):
    length = len(line)

    for p in range(kl, length):
        s = set(line[p-kl:p])
        if len(s) == kl:
            return p
 
def puzzle(file):
    line = file.readline()

    print(find_key(line,4))
    print(find_key(line,14))

def main():
    file_name = getfilename()

    with open(file_name, "r") as file:
        puzzle(file)

if __name__ == "__main__":
    main()

