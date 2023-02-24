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
    knot = [[0,0]]*10 # [x,y]

    visited = [[[0,0]]]*10

    data = file.read().splitlines()

    for op in data:
        d,l = op.split()
        l = int(l)
        print(d,l)

        match d:
            case 'R':
                for i in range(0,l):
                    knot[0] = [knot[0][x]+1, knot[0][y]]
                    for i in range(0,9):
                        ch,ct = i, i+1 # current_head, current_tail
                        if knot[ch][x] - knot[ct][x] >= 2:
                            knot[ct] = [knot[ct][x]+1, knot[ch][y]]
                            if knot[ct] not in visited[ct]:
                                visited[ct].append(knot[ct])
            case 'L':
                for i in range(0,l):
                    knot[0] = [knot[0][x]-1, knot[0][y]]
                    for i in range(0,9):
                        ch,ct = i, i+1 # current_head, current_tail
                        while knot[ct][x] - knot[ch][x] >= 2:
                            knot[ct] = [knot[ct][x]-1, knot[ch][y]]
                            if knot[ct] not in visited[ct]:
                                visited[ct].append(knot[ct])
            case 'U':
                knot[0] = [knot[0][x], knot[0][y]+l]
                for i in range(0,9):
                    ch,ct = i, i+1 # current_head, current_tail
                    while knot[ch][y] - knot[ct][y] >= 2:
                        knot[ct] = [knot[ch][x], knot[ct][y]+1]
                        if knot[ct] not in visited[ct]:
                            visited[ct].append(knot[ct])
            case 'D':
                knot[0] = [knot[0][x], knot[0][y]-l]
                for i in range(0,9):
                    ch,ct = i, i+1 # current_head, current_tail
                    while knot[ct][y] - knot[ch][y] >= 2:
                        knot[ct] = [knot[ch][x], knot[ct][y]-1]
                        if knot[ct] not in visited[ct]:
                            visited[ct].append(knot[ct])

    for i in range(0,10):
        print(i, len(visited[i]))

def main():
    file_name = getfilename()

    with open(file_name, "r") as file:
        puzzle(file)

if __name__ == "__main__":
    main()

