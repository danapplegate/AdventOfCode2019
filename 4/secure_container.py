#!/usr/bin/env python3

range_start = 147981
range_end = 691423


def test(number: int) -> bool:
    n = str(number)
    d = n[0]
    repeated = False
    for digit in n[1:]:
        if digit < d:
            return False
        if d == digit:
            repeated = True
        d = digit
    return repeated


num_found = 0
for n in range(range_start, range_end + 1):
    if test(n):
        num_found += 1

print(f"Num found: {num_found}")
