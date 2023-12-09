with open("input.txt") as file:
    str_in = file.read()

lines = str_in.splitlines()
differences = []
for line in lines:
    cur_nums = [int(i) for i in line.split(" ")]
    differences.append([cur_nums])

    while sum([1 for i in cur_nums if i != 0]):
        new_dif = [j-i for i,j in zip(cur_nums[:-1], cur_nums[1:])]
        cur_nums = new_dif
        differences[-1].append(cur_nums)

    for (bottom, top) in zip(differences[-1][::-1][:-1], differences[-1][::-1][1:]):
        top.append(top[-1] + bottom[-1])

    for (bottom, top) in zip(differences[-1][::-1][:-1], differences[-1][::-1][1:]):
        top.insert(0, top[0] - bottom[0])

s = sum([*map(lambda x:x[0][-1], differences)])
print(s)

s = sum([*map(lambda x:x[0][0], differences)])
print(s)