#!/usr/bin/env python3
from math import floor


def calc_fuel(mass: int):
    fuel_req: int = floor(mass / 3) - 2
    if fuel_req <= 0:
        return 0
    else:
        return fuel_req + calc_fuel(fuel_req)


with open("./input.txt") as f:
    masses: list = [int(line) for line in f]
    fuel: int = sum([floor(mass / 3) - 2 for mass in masses])
    print(f"Base fuel requirement: {fuel}")
    print(f"Extended fuel requirement: {sum([calc_fuel(mass) for mass in masses])}")

