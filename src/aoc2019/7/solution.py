#!/usr/bin/env python3
#from ..intcode import Program, local_resolver
import sys
from io import StringIO


if __name__ == "__main__":
    print(sys.path)
    sys.stdin = StringIO()
    sys.stdin.write("Testing\n")
    sys.stdin.seek(0)
    response = input("What?")
    print(response)