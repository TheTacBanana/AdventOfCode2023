from typing import DefaultDict
from math import lcm

with open("input.txt") as file:
    str_in = file.read()

mapping = {}
instructions, _, *lines = str_in.splitlines()
for line in lines:
    f, rhs = line.split(" = ")
    l, r = rhs[1:-1].split(", ")
    mapping[f] = (l, r)

def find(fr, to):
    visited = set()
    total_count, pc, inst = 0, 0, fr
    while True:
        total_count += 1
        inst = mapping[inst][instructions[pc] == "R"]
        if (inst, pc) in visited:
            return None
        if inst == to:
            break
        visited.add((inst, pc))
        pc = (pc + 1) % len(instructions)
    return total_count
print(find("AAA", "ZZZ"))

start = [i for i in mapping.keys() if i[-1] == "A"]
end = [i for i in mapping.keys() if i[-1] == "Z"]

steps = DefaultDict(dict)
for s in start:
    for e in end:
        n = find(s, e)
        if n is not None:
            steps[s][e] = n

min_cycle = lcm(*(min(steps[k].values()) for k in steps.keys()))
print(min_cycle)