with open("input.txt") as file:
    str_in = file.read().strip()

lines = str_in.splitlines()

start = None
grid = [[j for j in i] for i in lines]
for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == "S":
            start = (c, r)

width = len(grid[0])
height = len(grid)

from functools import cache
@cache
def adjacent(pos):
    px, py = pos
    return 

goal = 26501365

x = []
y = []
currently_on = {start}
for i in range(1,1000):
    print(i)
    new_on = set()

    for px, py in currently_on:
        for ox, oy in ((0, -1),(1, 0),(0, 1),(-1, 0)):
            nx = px + ox
            ny = py + oy
            if grid[ny % height][nx % width] != "#":
                new_on.add((nx, ny))
    currently_on = new_on
    
    if i == 64:
        print(len(currently_on))
    if i % height == goal % height:
        print(i, len(currently_on))
        x.append(i)
        y.append(len(currently_on))
        if len(x) == 3:
            break

c0 = y[0]
c1a = (y[1] - y[0]) / (x[1] - x[0])
c1b = (y[2] - y[1]) / (x[2] - x[1])
c2 = (c1b - c1a) / (x[2] - x[0])
p2 = c0 + c1a * (goal - x[0]) + c2 * (goal - x[0]) * (goal - x[1])
print(int(p2))