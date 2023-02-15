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

def is_visible(height, row, col, data):
    rows = len(data)
    cols = len(data[0])

    if row == 0 or row == rows-1 or col == 0 or col == cols-1:
        # on the edge, so visible
        return 1

    # check row
    heights = data[row]
    if max(heights[0:col]) < height or max(heights[col + 1:]) < height:
        return 1

    # check column
    heights = [row[col] for row in data]
    if max(heights[0:row]) < height or max(heights[row+1:]) < height:
        return 1

    return 0

def get_score(height, row, col, data):
    rows = len(data)
    cols = len(data[0])
    tot_score = 1

    if row == 0 or row == rows-1 or col == 0 or col == cols-1:
        # on the edge, so scenic score of zero
        return 0

    # heights left, right, up, down
    trees4 = [
                data[row][0:col][::-1], data[row][col+1:],
                [row[col] for row in data][0:row][::-1],
                [row[col] for row in data][row+1:]
            ]
    for trees in trees4:
        score = 0
        for tree in trees:
            score += 1
            if tree >= height:
                break
        tot_score *= score

    return tot_score

def puzzle(file):
    data = file.read().split()

    visibles = 0
    hiscore = hicol = hirow = 0
    for row, row_heights in enumerate(data):
        for col, height in enumerate(row_heights):
            visibles += is_visible(height, row, col, data)
            score = get_score(height, row, col, data)
            if score > hiscore:
                hiscore, hirow, hicol = score, row, col
            hiscore = max(score, hiscore)
            print(height, end="")
        print()
    print("visible trees:", visibles)
    print("Hiscore at", hirow, hicol, ":", hiscore)

def main():
    file_name = getfilename()

    with open(file_name, "r") as file:
        puzzle(file)

if __name__ == "__main__":
    main()

