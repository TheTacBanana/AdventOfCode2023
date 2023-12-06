with open("input.txt") as file:
    str_in = file.read()

sum = 0
lines = str_in.splitlines()
for row in range(len(lines)):

    validNum = False
    curNum = ""
    for col in range(len(lines[0])):
        c = lines[row][col]
        if c.isnumeric():
            curNum += c

            for i in range(-1,2):
                for j in range(-1,2):
                    try:
                        c = lines[row + i][col + j]
                        if not c.isnumeric() and c != ".":
                            validNum = True
                    except:
                        k = None

        elif curNum != "":
            if validNum:
                sum += int(curNum)
            curNum = ""
            validNum = False
    if curNum != "":
        if validNum:
            sum += int(curNum)
        curNum = ""
        validNum = False
        
print()
print(sum)

gears = {}

sum = 0
lines = str_in.splitlines()
for row in range(len(lines)):

    gearedOn = set()
    curNum = ""
    for col in range(len(lines[0])):
        c = lines[row][col]
        if c.isnumeric():
            curNum += c

            for i in range(-1,2):
                for j in range(-1,2):
                    try:
                        c = lines[row + i][col + j]
                        if not c.isnumeric() and c == "*":
                            gearedOn.add((row + i, col + j))
                    except:
                        k = None

        elif curNum != "":
            for g in gearedOn:
                if g not in gears:
                    gears[g] = [int(curNum)]
                else:
                    gears[g].append(int(curNum))
            gearedOn = set()
            curNum = ""
    if curNum != "":
        for g in gearedOn:
            if g not in gears:
                gears[g] = [int(curNum)]
            else:
                gears[g].append(int(curNum))
        gearedOn = set()
        curNum = ""

sum = 0

for gear in gears:
    xs = gears[gear]
    if len(xs) == 2:
        sum += xs[0] * xs[1]
        print(xs[0], xs[1])


print(gears)

print()
print(sum)