from json import loads
from copy import deepcopy
from math import prod

class Workflow():
    def __init__(self, string) -> None:
        split_index = string.index("{")
        self.name = string[:split_index]
        processes = string[split_index + 1: -1].split(",")
        processes_out = []
        comparisons = []
        for process in processes:
            c = None
            if "A" == process:
                p = (0,)
            elif "R" == process:
                p = (1,)
            elif ":" in process:
                lhs, rhs = process.split(":")
                p = (2, eval(f"lambda part : part.{lhs}"), rhs)
                c = (lhs[0], -1 if lhs[1] == "<" else 1, int(lhs[2:]))
            else:
                p = (3, process)
            processes_out.append(p)
            comparisons.append(c)

        self.processes = processes_out
        self.comparisons = comparisons

    def process_part(self, part):
        for p in self.processes:
            match p[0]:
                case 0:
                    return "A"
                case 1:
                    return "R"
                case 2:
                    if p[1](part):
                        return p[2]
                case 3:
                    return p[1]

class Part():
    def __init__(self, string) -> None:
        n_s = string.replace(",",",\"").replace("=","\":").replace("{","{\"")
        loaded = loads(n_s)

        self.x = loaded["x"]
        self.m = loaded["m"]
        self.a = loaded["a"]
        self.s = loaded["s"]

    def value(self):
        return self.x + self.m + self.a + self.s

with open("input.txt") as file:
    str_in = file.read().strip()

workflows_str, parts_str = str_in.split("\n\n")

workflows = {(w:=Workflow(s)).name:w for s in workflows_str.splitlines()}
parts = [Part(s) for s in parts_str.splitlines()]

accepted_parts = []
for part in parts:
    cur_workflow = "in"

    finished = False
    while not finished:
        result = workflows[cur_workflow].process_part(part)
        match result:
            case "A":
                accepted_parts.append(part)
                finished = True
            case "R":
                finished = True
            case _:
                cur_workflow = result

p1 = [p.value() for p in accepted_parts]
p1 = sum(p1)
print(p1)

class RangedPart():
    def __init__(self) -> None:
        self.ranges = {x:(1, 4000) for x in "xmas"}

    def split(p, c, dir, n):
        l, r = p.ranges[c]

        n_position = None
        if n < l:
            n_position = -1
        elif n >= l and n <= r:
            n_position = 0
        elif n > r:
            n_position = 1

        if dir == -1:
            match n_position:
                case -1:
                    return p, None
                case 0:
                    cloned = deepcopy(p)
                    p.ranges[c] = (l, n -1)
                    cloned.ranges[c] = (n, r)
                    return cloned, p
                case 1:
                    return None, p

        elif dir == 1:
            match n_position:
                case -1:
                    return None, p
                case 0:
                    cloned = deepcopy(p)
                    p.ranges[c] = (n+1, r)
                    cloned.ranges[c] = (l, n)
                    return cloned, p
                case 1:
                    return p, None

    def combinations(self):
        return prod(map(lambda x : x[1] - x[0] + 1, self.ranges.values()))

def traverse_workflow(wf, parts_in = [RangedPart()]):
    match wf:
        case "A":
            return parts_in
        case "R":
            return []

    cur_wf = workflows[wf]
    end_accepted = []
    parts = deepcopy(parts_in)
    for i, process in enumerate(cur_wf.processes):
        match process[0]:
            case 0:
                end_accepted.extend(parts)
                return end_accepted
            case 1:
                return end_accepted
            case 2:
                unnacepted_parts = []
                accepted_parts = []
                for p in parts:
                    c, dir, n = cur_wf.comparisons[i]
                    u, a = RangedPart.split(p, c, dir, n)
                    if u != None:
                        unnacepted_parts.append(u)
                    if a != None:
                        accepted_parts.append(a)
                parts = unnacepted_parts
                end_accepted.extend(traverse_workflow(process[2], accepted_parts))
            case 3:
                end_accepted.extend(traverse_workflow(process[1], parts))
    return end_accepted

p2 = traverse_workflow("in")
p2 = sum([p.combinations() for p in p2])
print(p2)