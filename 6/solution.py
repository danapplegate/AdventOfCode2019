#!/usr/bin/env python3
from collections import defaultdict
import argparse


def count_orbits(graph, target, depth):
    if target not in graph:
        return depth
    sub_orbits = {}
    for sub_orbit in graph[target]:
        sub_orbits[sub_orbit] = count_orbits(graph, sub_orbit, depth + 1)
    return depth + sum(sub_orbits.values())
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solves the Universal Orbit Map problem")
    parser.add_argument("filename", type=argparse.FileType("r"))

    args = parser.parse_args()

    graph = defaultdict(list)
    for line in args.filename:
        line = line.strip()
        orbitee, orbiter = line.split(")")
        graph[orbitee].append(orbiter)
    total_orbits = count_orbits(graph, "COM", 0)
    print(f"Total orbits: {total_orbits}")