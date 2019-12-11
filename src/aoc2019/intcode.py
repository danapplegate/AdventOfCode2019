from typing import List


def process(mem: List[int], pos: int) -> bool:
    instruction = str(mem[pos])
    opcode = int(instruction[-2:], 10)
    parameter_modes = instruction[:-2]
    if opcode == 99:
        return False
    elif opcode in [1, 2]:
        param1, param2, dest = mem[pos + 1 : pos + 4]
        if len(parameter_modes) < 1 or parameter_modes[-1] == "0":
            param1 = mem[param1]
        if len(parameter_modes) < 2 or parameter_modes[-2] == "0":
            param2 = mem[param2]

        if opcode == 1:
            mem[dest] = param1 + param2
        elif opcode == 2:
            mem[dest] = param1 * param2
        return 4
    elif opcode in [3, 4]:
        param = mem[pos + 1]
        if opcode == 3:
            arg = int(input("Provide an integer input: "))
            mem[param] = arg
        elif opcode == 4:
            if len(parameter_modes) < 1 or parameter_modes[-1] == "0":
                param = mem[param]
            print(f"Output: {param}")
        return 2
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
        step = process(mem, ip)
        while step:
            ip += step
            step = process(mem, ip)

        return mem[0]
