#!/usr/bin/env python3
from intcode import Program
import itertools

p = Program()
for noun, verb in itertools.product(range(100), range(100)):
    print(f"Running program with inputs {noun} and {verb}...")
    if p.run(noun, verb) == 19690720:
        print("Success!")
        exit(0)
print("No match found")