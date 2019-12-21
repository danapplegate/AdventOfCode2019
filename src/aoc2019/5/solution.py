#!/usr/env/bin python3
from os import path
from ..intcode import Program, local_resolver
import sys


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Solves the Sunny With a Chance of Asteroids problem"
    )
    parser.add_argument(
        "-f", "--filename", type=local_resolver(__file__), default="input.txt", required=False
    )

    args = parser.parse_args()

    p = Program(args.filename)
    p.run()
