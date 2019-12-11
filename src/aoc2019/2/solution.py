#!/usr/bin/env python3
from ..intcode import Program
import itertools
from os import path


if __name__ == "__main__":
    filename = path.abspath(path.join(path.dirname(__file__), "input.txt"))
    p = Program(filename)
    for noun, verb in itertools.product(range(100), range(100)):
        print(f"Running program with inputs {noun} and {verb}...")
        if p.run(noun, verb) == 19690720:
            print("Success!")
            exit(0)
    print("No match found")
