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

def has_numbers(string):
    return any(char.isdigit() for char in string)

def puzzle(file):
    depth = 0
    tot = 0
    sizes = []
    dirs = []
    counted_dirs = []

    for line in file:
        tokens = line.split()
        if tokens[0] == "$":
            if tokens[1] == "cd":
                if tokens[2] == "..":
                    # go up
                    if sizes[-1] <= 100000:
                        tot += sizes[-1]
                        counted_dirs.append((dirs[-1], sizes[-1]))
                        print("counted_dirs:", counted_dirs)
                    sizes[-2] += sizes[-1]
                    depth -= 1
                    print(depth*"   ", dirs[-2], ":", sizes[-2], "(+", sizes[-1], ")")
                    sizes.pop()
                    dirs.pop()
                else:
                    # go down
                    depth += 1
                    sizes.append(0)
                    dirs.append(tokens[2])
                    print(depth*"   ", dirs[-1], ":", sizes[-1])
        elif has_numbers(tokens[0]):
            # count size 
            sizes[-1] += int(tokens[0])
            print(depth*"   ", dirs[-1], ":", sizes[-1], "(+", int(tokens[0]), ")")

    # ascend to root
    while len(sizes) > 1:
        if sizes[-1] <= 100000:
            tot += sizes[-1]
            counted_dirs.append((dirs[-1], sizes[-1]))
            print("counted_dirs:", counted_dirs)
        sizes[-2] += sizes[-1]
        depth -= 1
        print(depth*"   ", dirs[-2], ":", sizes[-2], "(+", sizes[-1], ")")
        sizes.pop()
        dirs.pop()

    cs = 0
    for _, s in counted_dirs:
        cs += s
    print(f"Total: {tot}, counted_dirs: {cs}")

def main():
    file_name = getfilename()

    with open(file_name, "r") as file:
        puzzle(file)

if __name__ == "__main__":
    main()

