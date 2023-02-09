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

def dir_size(d, data = None):
    print(d.depth*"  ", d.name, d.size)

def count_small_dirs(d = None, data = None):
    if not hasattr(count_small_dirs, "sum"):
        count_small_dirs.sum = 0

    if d != None:
        if d.size <= 100000:
            count_small_dirs.sum += d.size
            print(d.depth*"   ", d.name, d.size)

    return count_small_dirs.sum

def smallest_to_del(d = None, to_del = None):
    if not hasattr(smallest_to_del, "smallest"):
        smallest_to_del.smallest = None

    if d == None and to_del == None:
        return smallest_to_del.smallest.name, smallest_to_del.smallest.size

    if smallest_to_del.smallest == None:
        if d.size >= to_del:
            smallest_to_del.smallest = d
            print(d.depth*"   ", d.name, d.size)
    else:
        if d.size >= to_del and d.size < smallest_to_del.smallest.size:
            smallest_to_del.smallest = d
            print(d.depth*"   ", d.name, d.size)

    

class DirTree:
    def __iniit__(self):
        self.tree = None

    def add_subdir(self, name):
        subdir = DirNode(name)
        self.tree = subdir
        return subdir

    def traverse(self, preop=None, postop=None, data = None): # depth first
        self.tree.traverse(preop, postop, data)

    def size(self):
        if self.tree:
            return self.tree.size
        else:
            return 0

class DirNode:
    def __init__(self, name, parent=None):
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

    def traverse(self, preop=None, postop=None, data = None): # depth first
        if preop:
            preop(self, data)
        for subdir in self.subdirs:
            subdir.traverse(preop, postop, data)
        if postop:
            postop(self, data)

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
                    size = current_dir.size

                    current_dir.parent.size += size
                    current_dir = current_dir.parent
                    print(current_dir.depth*"   ", current_dir.name , ":", current_dir.size, "( +", size, ")")
                else:
                    # go down
                    current_dir = current_dir.add_subdir(tokens[2])
                    print(current_dir.depth*"   ", current_dir.name , ":", current_dir.size)
        elif has_numbers(tokens[0]):
            # count size 
            size = int(tokens[0])
            current_dir.size += size
            print(current_dir.depth*"   ", current_dir.name , ":", current_dir.size, "( +", size, ")")

    # ascend to root in case we are not back there
    while current_dir.parent != None:
        # go up
        size = current_dir.size

        current_dir.parent.size += size
        current_dir = current_dir.parent
        print(current_dir.depth*"   ", current_dir.name , ":", current_dir.size, "( +", size, ")")

    print("\ntraversing the tree top-down")
    tree.traverse(preop=dir_size)
    print("\n traversing the tree bottom-up")
    tree.traverse(postop=dir_size)

    print("\nCounting dirs < 100000")
    tree.traverse(count_small_dirs)
    print("total:", count_small_dirs())

    # Part 2
    disk_size = 70000000
    needed_space = 30000000

    unused = disk_size - tree.size()
    to_delete = needed_space - unused # Assuming we always have to delete something

    print("\nFinding smallest dir to delete")
    tree.traverse(preop=smallest_to_del, data = to_delete)
    print("Smallest dir:", smallest_to_del())

def main():
    file_name = getfilename()

    with open(file_name, "r") as file:
        puzzle(file)

if __name__ == "__main__":
    main()

