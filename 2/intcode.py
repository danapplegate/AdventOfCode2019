from typing import List


def process(mem: List[int], pos: int) -> bool:
    instruction: List[int] = mem[pos : pos + 4]
    opcode, param1, param2, dest = instruction
    if opcode == 99:
        return False
    elif opcode == 1:
        mem[dest] = mem[param1] + mem[param2]
    elif opcode == 2:
        mem[dest] = mem[param1] * mem[param2]
    else:
        raise Exception(f"Invalid opcode {opcode} at position {pos}")
    return True


class Program:
    """An IntCode program, represented by a list of instructions. Execute by calling run() with a pair of inputs."""

    p: List[int]

    def __init__(self, filename: str = "./input.txt"):
        with open(filename) as f:
            self.p = [int(n) for n in f.readline().split(",")]

    def run(self, noun, verb) -> int:
        if self.p is None:
            raise Exception("No program loaded")
        mem: List[int] = self.p.copy()
        mem[1] = noun
        mem[2] = verb

        ip: int = 0
        while process(mem, ip):
            ip += 4

        return mem[0]
