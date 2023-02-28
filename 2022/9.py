#!/usr/bin/python3
#jdfjkdsf

import os
import sys
import re
import copy
from operator import add, sub

X,Y = 0,1

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


DIRS = {
    "R": (1,0),
    "L": (-1,0),
    "U": (0,1),
    "D": (0,-1)
}

def ADD(a,b):
    return (a[X]+b[X], a[Y]+b[Y])

def SUB(a,b):
    return (a[X]-b[X], a[Y]-b[Y])

def cmp(a,b):
    if a[X] == b[X]: x = 0
    elif a[X] < b[X] : x = -1
    else: x = 1
    if a[Y] == b[Y]: y = 0
    elif a[Y] < b[Y] : y = -1
    else: y = 1
    return (x,y)

def move(head, tail):
    movement = cmp(head,tail) # How should the tail move (+/-1, +/-1) if needed
    diff = SUB(head,tail) # what's the gap between the head and tail
    if movement == diff: # the tail is close to the had and doesn't have to move
        return tail
    return ADD(tail, movement)

def print_map(knots):
    xs = [ knot[X] for knot in knots ]
    ys = [ knot[Y] for knot in knots ]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)

    rows = [ [' ']*(xmax-xmin+1) for _ in range(ymax-ymin+1)] 
    for i,knot in enumerate(knots):
        rows[knot[Y]-ymin][knot[X]-xmin] = str(i)

    for row in reversed(rows):
        print("".join(row))
    print("---")

    return

def puzzle(file):
    knots = [(0,0) for _ in range(10)]# (x,y)

    visited = [{(0,0)} for _ in range(10)] # using a set to get rid of duplicates

    print_map(knots)

    data = file.read().splitlines()

    for op in data:
        dir,step = op.split()
        step = int(step)
        print(dir,step)

        for i in range(0,step):
            knots[0] = ADD(knots[0], DIRS[dir])
            visited[0].add(knots[0])

            for j in range(0,9):
                knots[j+1] = move(knots[j], knots[j+1])
                visited[j+1].add(knots[j+1])

        print_map(knots)

    for i, knot in enumerate(visited):
        print(i, len(knot))

def main():
    file_name = getfilename()

    with open(file_name, "r") as file:
        puzzle(file)

if __name__ == "__main__":
    main()

