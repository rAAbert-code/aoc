#!/usr/bin/python3
#jdfjkdsf

import os
import sys
import re
import copy
from operator import add, sub

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
    x,y = 0,1
    h = t = [0,0] # [x,y]
    visited = [t]

    data = file.read().splitlines()

    print(h, t)
    for op in data:
        d,l = op.split()
        l = int(l)
        print(d,l)

        match d:
            case 'R':
                h = [h[x]+l, h[y]]
                while  h[x] - t[x] >= 2:
                    t = [t[x]+1, h[y]]
                    if t not in visited:
                        visited.append(t)
            case 'L':
                h = [h[x]-l, h[y]]
                while t[x] - h[x] >= 2:
                    t = [t[x]-1, h[y]]
                    if t not in visited:
                        visited.append(t)
            case 'U':
                h = [h[x], h[y]+l]
                while h[y] - t[y] >= 2:
                    t = [h[x], t[y]+1]
                    if t not in visited:
                        visited.append(t)
            case 'D':
                h = [h[x], h[y]-l]
                while t[y] - h[y] >= 2:
                    t = [h[x], t[y]-1]
                    if t not in visited:
                        visited.append(t)
        print(h, t)

    print("#:", len(visited))

        

def main():
    file_name = getfilename()

    with open(file_name, "r") as file:
        puzzle(file)

if __name__ == "__main__":
    main()

