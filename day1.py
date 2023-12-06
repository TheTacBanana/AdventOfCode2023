from copy import copy

with open("input.txt") as file:
    str_in = file.read()

count = 0
for line in str_in.splitlines():
    nums = list(filter(lambda x : x.isnumeric(), line))
    count += int(nums[0] + nums[-1])
print(count)

mapping = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
}

total = 0
for line in str_in.splitlines():
    out = []
    for i in range(len(line)):
        c = line[i]
        if line[i].isnumeric():
            out.append(line[i])
        for txt, val in mapping.items():
            if line[i:].startswith(txt):
                out.append(val)

    total += int(out[0] + out[-1])
print(total)