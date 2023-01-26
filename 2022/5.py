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

def get_indeces(line):
    return [i for i, ltr in enumerate(line) if ltr == '[']

def add_to_stack(stacks, t, ch):
    if t > len(stacks):
        for i in range(len(stacks), t):
            stacks.append("")
    stacks[t - 1] = ch + stacks[t - 1] 

def get_stacks(stacks, file):
    for line in file:
        indeces = get_indeces(line)
        if not indeces:
            return # This will discard the current line (with stack numbers)
        for i in indeces:
            ch = line[i+1]
            t = i // 4 + 1 # Each column is 4 char wide
            add_to_stack(stacks, t, ch)

def make_move(stacks, num, f, t, mc = False):
    if mc:
        to_move = stacks[f - 1][-num:]
    else:
        to_move = stacks[f - 1][:-num-1:-1] # reversed so we can just add to the to_stack
    stacks[f - 1] = stacks[f - 1][:-num]
    stacks[t - 1] += to_move

def make_moves(file, s1, s2):
    for line in file:
        _, num, _, f, _, t = line.split()
        num, f, t = int(num), int(f), int(t)
        make_move(s1, num, f, t, False)
        make_move(s2, num, f, t, True)


def get_tops(stacks):
    return ''.join([st[-1] for st in stacks])

def puzzle(file):
    stacks1, stacks2 = [], []
    get_stacks(stacks1, file)
    stacks2 = copy.deepcopy(stacks1)

    file.readline() # Get rid of empty line
    
    make_moves(file, stacks1, stacks2)

    tops1 = get_tops(stacks1)
    tops2 = get_tops(stacks2)
    print(tops1)
    print(tops2)

def main():
    file_name = getfilename()

    with open(file_name, "r") as file:
        puzzle(file)

if __name__ == "__main__":
    main()

