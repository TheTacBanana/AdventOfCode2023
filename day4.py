with open("input.txt") as file:
    str_in = file.read()

total = 0
lines = str_in.splitlines()
results = [[0, 0] for i in range(len(lines))]
for (i, line) in enumerate(lines):
    _, nums = line.split(": ")
    lhs, rhs = nums.split("|")

    lhs = {int(i) for i in lhs.split(" ") if i != ""}
    rhs = {int(i) for i in rhs.split(" ") if i != ""}

    import math
    total = len(lhs.intersection(rhs))
    val = math.floor(2 ** (total - 1))
    print(val)
    results[i][0] = val
    results[i][1] += 1

    for j in range(i + 1, i + 1 + total):
        if j < len(results):
            results[j][1] += 1 * results[i][1]

    print(results)

print(sum(i[0] for i in results))
print(sum(i[1] for i in results))