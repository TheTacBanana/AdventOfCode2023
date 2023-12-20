from collections import deque
from dataclasses import dataclass
from math import gcd, prod
from typing import Any

BROADCAST = "broadcaster"
FLIP_FLOP = "%"
CONJUNCTION = "&"

@dataclass
class Module:
    type: str
    mem: Any
    out: list[str]

    def process(self, fr, pulse):
        if self.type == BROADCAST:
            return pulse
        elif self.type == FLIP_FLOP:
            if pulse == True:
                return None
            else:
                is_on = bool(self.mem)
                self.mem = not is_on
                return not is_on
        elif self.type == CONJUNCTION:
            self.mem[fr] = pulse
            all_high = all(x == True for x in self.mem.values())
            return not all_high

def parse(string):
    lhs, rhs = string.split(" -> ")
    dest = rhs.split(", ")
    if "%" in lhs:
        return lhs[1:], Module(type=FLIP_FLOP, mem=False, out=dest)
    elif "&" in lhs:
        return lhs[1:], Module(type=CONJUNCTION, mem={}, out=dest)
    elif "broadcaster" in lhs:
        return BROADCAST, Module(type=BROADCAST, mem=None, out=dest)

with open("input.txt") as file:
    str_in = file.read().strip()

modules = {k:v for k,v in (parse(line) for line in str_in.splitlines())}

for ident, mod in modules.items():
    for dest in mod.out:
        d_mod = modules.get(dest)
        if d_mod and d_mod.type == CONJUNCTION:
            d_mod.mem[ident] = False

cycles = {}
total = [0, 0]
i = 0
while True:
    if i == 1000:
        print(total[0] * total[1])

    q = deque([("button", BROADCAST, False)])
    while q:
        fr, to, pulse = q.popleft()
        total[pulse] += 1

        cur_module = modules.get(to)
        if cur_module is None:
            continue

        new_pulse = cur_module.process(fr, pulse)

        if (to in {"dc", "rv", "vp", "cq"} and new_pulse == True):
            if to not in cycles:
                cycles[to] = i + 1

        if len(cycles) == 4:
            deltas = list(cycles.values())
            lcm = prod(deltas) // gcd(*deltas)
            print(lcm)
            quit()

        if new_pulse is not None:
            for dst_identifier in cur_module.out:
                q.append((to, dst_identifier, new_pulse))
    i += 1