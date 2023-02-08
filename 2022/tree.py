#!/usr/bin/python3
#jdfjkdsf

import os
import sys
import re
import copy

def getfilename():
    args = sys.argv
    dir_name = os.path.dirname(args[0])
    file_name = os.path.basename(args[0]).split(".")[0]
    if len(args) < 2:
        file_name += ".data"
    elif args[1] == "-s":
        file_name += ".sample"
    else:
        sys.exit("Unknown argument")
    return dir_name + "/input/" + file_name

class DirTree:
    def __iniit__(self):
        self.tree = None

    def add_subdir(self, name):
        subdir = DirNode(name)
        self.tree = subdir
        return subdir

    def traverse(self): # depth first
        self.tree.traverse()

class DirNode:
    def __init__(self, name, parent=None, preop = None, postop=None):
        self.name = name
        self.size = 0
        self.subdirs = []
        self.parent = parent
        if self.parent == None:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1

    def add_subdir(self, name):
        subdir = DirNode(name, self)
        self.subdirs.append(subdir)
        return subdir

    def traverse(self): # depth first
        print(self.depth*"  ", self.name, self.size)
        for subdir in self.subdirs:
            subdir.traverse()

def has_numbers(string):
    return any(char.isdigit() for char in string)

def puzzle(file):
    depth = 0
    tree = DirTree()
    current_dir = tree

    for line in file:
        tokens = line.split()
        if tokens[0] == "$":
            if tokens[1] == "cd":
                if tokens[2] == "..":
                    # go up
                    current_dir.parent.size += current_dir.size
                    current_dir = current_dir.parent
                    print(current_dir.depth*"   ", current_dir.name , ":", current_dir.size)
                else:
                    # go down
                    current_dir = current_dir.add_subdir(tokens[2])
                    print(current_dir.depth*"   ", current_dir.name , ":", current_dir.size)
        elif has_numbers(tokens[0]):
            # count size 
            size = int(tokens[0])
            current_dir.size += size
            print(current_dir.depth*"   ", current_dir.name , ":", current_dir.size, "( +", size, ")")

    # ascend to root
    while current_dir.parent != None:
        # go up
        current_dir.parent.size += current_dir.size
        current_dir = current_dir.parent
        print(current_dir.depth*"   ", current_dir.name , ":", current_dir.size)

    print("\n traversing the tree.")
    tree.traverse()

    # Part 2

def main():
    file_name = getfilename()

    with open(file_name, "r") as file:
        puzzle(file)

if __name__ == "__main__":
    main()

