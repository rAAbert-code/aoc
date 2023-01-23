#!/usr/bin/python3


import sys

stacks = []

def getfilearg():
    args = sys.argv
    if len(args) < 2:
        print("Please supply name of input data file")
        exit()
    return args[1]

def get_indeces(line):
    return [i for i, ltr in enumerate(line) if ltr == '[']

def get_stacks(stacks, file):
    for line in file:
        indeces = get_indeces(line)
        if not indeces:
            return
        for i in indeces:
            ch = line[i+1]
            stack = i // 4 + 1
            print(stack, ch )

def puzzle(file):
    get_stacks(stacks, file)
    for line in file:
        print(line.rstrip())


def main():
    file_name = getfilearg()

    with open(file_name, "r") as file:
        puzzle(file)

if __name__ == "__main__":
    main()

