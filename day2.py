with open("input.txt") as file:
    str_in = file.read()

total_cubes = {
    "red" : 12,
    "green" : 13,
    "blue" : 14,
}

max_taken = {
    "red" : 0,
    "green" : 0,
    "blue" : 0,
}

count = 0
power_total = 0
for line in str_in.splitlines():
    id, line = line.split(": ")
    id = int(id.split(" ")[1])

    split = line.split("; ")

    takes = []
    for pair in split:
        pairs = pair.split(", ")

        takes.append([])
        for j in pairs:
            val, colour = j.split(" ")
            val = int(val)
            takes[-1].append((val, colour))

    int_max_t = {
        "red" : 0,
        "green" : 0,
        "blue" : 0
    }

    valid = True
    for takelist in takes:
        taken = {
            "red" : 0,
            "green" : 0,
            "blue" : 0
        }

        for (val, colour) in takelist:
            total_cubes[colour] -= val
            taken[colour] += val

            if int_max_t[colour] < val:
                int_max_t[colour] = val

        for t in total_cubes:
            if (total_cubes[t] < 0):
                valid = False

        for (val, colour) in takelist:
            total_cubes[colour] += val
            taken[colour] -= val

    if valid:
        count += id
        print(int_max_t)

    mul = 1
    for t in int_max_t:
        print(t, int_max_t[t])
        if (int_max_t[t] != 0):
            mul *= int_max_t[t]
    print(mul)
    power_total += mul

print(count)
print(power_total)