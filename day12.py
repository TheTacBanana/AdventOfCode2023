from functools import cache

with open("input.txt") as file:
    str_in = file.read()

class Row:
    def __init__(self, pattern, counts):
        self.pattern = pattern
        self.counts = counts

@cache
def arrange(pattern, counts):
    if not pattern:
        return len(counts) == 0
    if not counts:
        return "#" not in pattern

    result = 0

    if pattern[0] in ".?":
        result += arrange(pattern[1:], counts)

    if (pattern[0] in "#?" and counts[0] <= len(pattern) and
        "." not in pattern[:counts[0]] and (counts[0] == len(pattern) or pattern[counts[0]] != "#")):
        result += arrange(pattern[counts[0] + 1:], counts[1:])

    return result


rows = []
for line in str_in.splitlines():
    lhs, rhs = line.split(" ")
    counts = tuple(int(x) for x in rhs.split(","))
    rows.append(Row(lhs, counts))

p1 = sum([arrange(row.pattern, row.counts) for row in rows])
print(p1)

rows = []
for line in str_in.splitlines():
    lhs, rhs = line.split(" ")
    pattern = "?".join([lhs] * 5)
    counts = tuple(int(x) for x in rhs.split(",")) * 5
    rows.append(Row(pattern, counts))

p2 = sum([arrange(row.pattern, row.counts) for row in rows])
print(p2)