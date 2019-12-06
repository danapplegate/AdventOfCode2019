#!/usr/bin/env python3
import sys
import numpy
import argparse
from typing import TextIO, List, Tuple

numpy.set_printoptions(threshold=sys.maxsize)

parser = argparse.ArgumentParser(
    description="Solve the AdventOfCode2019 Crossed Wires problem"
)

parser.add_argument("filename", type=open, help="Input file to open")
parser.add_argument("-d", help="Display visual representation", action="store_true")
parser.add_argument("-v", "--verbose", help="Verbose output", action="store_true")


def read_path(input_file: TextIO):
    return input_file.readline().strip().split(",")


def get_dimensions(*paths: List[str]) -> (int, int, int, int):
    x_upper = x_lower = y_upper = y_lower = 0
    for path in paths:
        x = y = 0
        # print(f"Computing bounds for {path}")
        for seg in path:
            # print(seg)
            if seg[0] == "R":
                x += int(seg[1:])
                x_upper = max(x, x_upper)
            elif seg[0] == "L":
                x -= int(seg[1:])
                x_lower = min(x, x_lower)
            elif seg[0] == "U":
                y += int(seg[1:])
                y_upper = max(y, y_upper)
            elif seg[0] == "D":
                y -= int(seg[1:])
                y_lower = min(y, y_lower)
            # print(
            #     f"X: {x}, Y: {y}, X_MIN: {x_lower}, X_MAX: {x_upper}, Y_MIN: {y_lower}, Y_MAX: {y_upper}"
            # )
    return abs(x_lower) + x_upper + 1, abs(y_lower) + y_upper + 1, abs(x_lower), y_upper


def plot_paths(grid, origin: Tuple[int], *paths: List[str]) -> List[Tuple[int]]:
    start_x, start_y = origin
    x = start_x
    y = start_y
    path_id = 0
    distances = []
    for path in paths:
        steps = 0
        for seg in path:
            length = int(seg[1:])
            if seg[0] == "R":
                for _ in range(length):
                    if grid[path_id][start_y][x] == 0:
                        grid[path_id][start_y][x] = steps
                    if path_id == 1 and grid[0][start_y][x] != 0:
                        distances.append(steps + grid[0][start_y][x])
                    x += 1
                    steps += 1
            elif seg[0] == "L":
                for _ in range(length):
                    if grid[path_id][start_y][x] == 0:
                        grid[path_id][start_y][x] = steps
                    if path_id == 1 and grid[0][start_y][x] != 0:
                        distances.append(steps + grid[0][start_y][x])
                    x -= 1
                    steps += 1
            # Y axis is reversed in matrix
            elif seg[0] == "U":
                for _ in range(length):
                    if grid[path_id][y][start_x] == 0:
                        grid[path_id][y][start_x] = steps
                    if path_id == 1 and grid[0][y][start_x] != 0:
                        distances.append(steps + grid[0][y][start_x])
                    y -= 1
                    steps += 1
            elif seg[0] == "D":
                for _ in range(length):
                    if grid[path_id][y][start_x] == 0:
                        grid[path_id][y][start_x] = steps
                    if path_id == 1 and grid[0][y][start_x] != 0:
                        distances.append(steps + grid[0][y][start_x])
                    y += 1
                    steps += 1
            start_x = x
            start_y = y
        # Need to mark the final position, since we don't mark the start
        grid[path_id][y][x] = steps
        if path_id == 1 and grid[0][y][x] != 0:
            distances.append(steps + grid[0][y][x])
        start_x, start_y = origin
        x = start_x
        y = start_y
        path_id += 1
    return distances


args = parser.parse_args()
f = args.filename
path1 = read_path(f)
path2 = read_path(f)
width, height, origin_x, origin_y = get_dimensions(path1, path2)
origin = (origin_x, origin_y)
print(f"W: {width}, H: {height}, OX: {origin_x}, OY: {origin_y}")

grid = numpy.zeros((2, height, width), dtype=numpy.int64)
distances = plot_paths(grid, origin, path1, path2)
# print(grid)
# print(path1, path2)
print(f"Origin: {origin}")
# print(distances)
print(f"Closest step distance: {min(distances)}")
