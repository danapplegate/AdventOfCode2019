#!/usr/bin/env python3

range_start = 147981
range_end = 691423


def test(number: int) -> bool:
    n = str(number)
    d = n[0]
    occurrences = dict()
    for digit in n[1:]:
        if digit < d:
            return False
        if d == digit:
            occurrences[digit] = occurrences.get(digit, 1) + 1
        d = digit
    return any([x == 2 for x in occurrences.values()])


num_found = 0
for n in range(range_start, range_end):
    if test(n):
        num_found += 1

print(f"Num found: {num_found}")
