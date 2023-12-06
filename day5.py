with open("input.txt") as file:
    str_in = file.read()

class Stage():
    def __init__(self) -> None:
        self.domain = []
        self.codomain = []

    def add(self, dstart : int, sstart : int, r : int) -> None:
        self.domain.append((sstart, sstart + r - 1))
        self.codomain.append((dstart, dstart + r - 1))

    def map(self, val) -> int:
        for (i, (bottom, top)) in enumerate(self.domain):
            if val >= bottom and val <= top:
                diff = val - bottom
                return self.codomain[i][0] + diff
        return val

    def rmap(self, val) -> int:
        for (i, (bottom, top)) in enumerate(self.codomain):
            if val >= bottom and val <= top:
                diff = val - bottom
                return self.domain[i][0] + diff
        return val

    def in_domain(self, val) -> bool:
        for (bottom, top) in self.domain:
            if val >= bottom and val <= top:
                return True
        return False

import itertools

lines = str_in.splitlines()
print(lines)
groups = [list(group) for k,
            group in
            itertools.groupby(lines, lambda x: x=="") if not k]
seeds = [int(i) for i in groups[0][0].split(": ")[1].split(" ")]

stages = []
for group in groups[1:]:
    stage = Stage()
    values = group[1:]

    for v in values:
        ds, ss, r = [int(i) for i in v.split(" ")]
        stage.add(ds, ss, r)

    stages.append(stage)

out = []
for seed in seeds:
    val = seed
    for stage in stages:
        val = stage.map(val)
    out.append(val)

print(min(out))


seedStage = Stage()
for index in range(0, len(seeds), 2):
    s = seeds[index]
    r = seeds[index + 1]
    seedStage.add(s, s, r)

stages.reverse()

i = 0
while True:
    val = i
    for stage in stages:
        val = stage.rmap(val)

    if seedStage.in_domain(val):
        print(i)
        break

    i += 1