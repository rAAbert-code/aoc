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
    left = right = up = down = 0


    if row == 0 or row == rows-1 or col == 0 or col == cols-1:
        # on the edge, so scenic scoe of zero
        return 0

    # heights left, right, up, down
    heights = [
                data[row][0:col][::-1], data[row][col+1:],
                [row[col] for row in data][0:row][::-1],
                [row[col] for row in data][row+1:]
              ]

    return 0

def puzzle(file):
    data_strings = file.read().split()
    data = []
    for line in data_strings:
        ints = [int(x) for x in line]
        data.append(ints)

    row = col = visibles = 0
    score = hiscore =score_col = score_row = 0
    for row_heights in data:
        for height in row_heights:
            visibles += is_visible(height, row, col, data)
            score = get_score(height, row, col, data)
            col += 1
            print(height, end="")
        row += 1
        col = 0
        print()
    print("visible trees:", visibles)

def main():
    file_name = getfilename()

    with open(file_name, "r") as file:
        puzzle(file)

if __name__ == "__main__":
    main()

