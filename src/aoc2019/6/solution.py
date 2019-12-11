#!/usr/bin/env python3
from collections import defaultdict
import argparse
from typing import List, Dict


def count_orbits(graph, target, depth):
    if target not in graph:
        return depth
    sub_orbits = {}
    for sub_orbit in graph[target]:
        sub_orbits[sub_orbit] = count_orbits(graph, sub_orbit, depth + 1)
    return depth + sum(sub_orbits.values())


def find_path(graph: Dict[str, List[str]], source: str, targets: List[str]) -> List[str]:
    for orbitee, orbiters in graph.items():
        if source in orbiters:
            if orbitee in targets:
                return [orbitee]
            return [orbitee] + find_path(graph, orbitee, targets)


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
    you_path = find_path(graph, "YOU", ["COM"])
    print(f"YOU path: {you_path}")
    san_path = find_path(graph, "SAN", you_path)
    print(f"SAN path: {san_path}")
    san_path.reverse()
    common_target = san_path[0]
    you_path = you_path[:you_path.index(common_target)]
    total_path = you_path + san_path
    print(f"Total path: {total_path}")
    total_transfers = len(total_path) - 1
    print(f"Total transfers: {total_transfers}")