from typing import List


def is_position_mode(parameter_num: int, parameter_modes: str) -> bool:
    return (
        len(parameter_modes) < parameter_num or parameter_modes[-parameter_num] == "0"
    )


def process(mem: List[int], pos: int) -> bool:
    instruction = str(mem[pos])
    opcode = int(instruction[-2:], 10)
    parameter_modes = instruction[:-2]
    if opcode == 99:
        return False
    elif opcode in [1, 2, 7, 8]:
        param1, param2, dest = mem[pos + 1 : pos + 4]
        if is_position_mode(1, parameter_modes):
            param1 = mem[param1]
        if is_position_mode(2, parameter_modes):
            param2 = mem[param2]

        if opcode == 1:
            mem[dest] = param1 + param2
        elif opcode == 2:
            mem[dest] = param1 * param2
        elif opcode == 7:
            if param1 < param2:
                mem[dest] = 1
            else:
                mem[dest] = 0
        elif opcode == 8:
            if param1 == param2:
                mem[dest] = 1
            else:
                mem[dest] = 0

        return pos + 4
    elif opcode in [5, 6]:
        param1, param2 = mem[pos + 1 : pos + 3]
        if is_position_mode(1, parameter_modes):
            param1 = mem[param1]
        if is_position_mode(2, parameter_modes):
            param2 = mem[param2]

        if opcode == 5 and param1 != 0:
            return param2
        elif opcode == 6 and param1 == 0:
            return param2
        else:
            return pos + 3
    elif opcode in [3, 4]:
        param = mem[pos + 1]
        if opcode == 3:
            arg = int(input("Provide an integer input: "))
            mem[param] = arg
        elif opcode == 4:
            if is_position_mode(1, parameter_modes):
                param = mem[param]
            print(f"Output: {param}")
        return pos + 2
    else:
        raise Exception(f"Invalid opcode {opcode} at position {pos}")


class Program:
    """An IntCode program, represented by a list of instructions. Execute by calling run() with a pair of inputs."""

    p: List[int]

    def __init__(self, filename: str):
        with open(filename) as f:
            self.p = [int(n) for n in f.readline().split(",")]

    def run(self, noun=None, verb=None) -> int:
        if self.p is None:
            raise Exception("No program loaded")
        mem: List[int] = self.p.copy()
        if noun:
            mem[1] = noun
        if verb:
            mem[2] = verb

        ip: int = 0
        ip = process(mem, ip)
        while ip is not False:
            ip = process(mem, ip)

        return mem[0]
