pipe_map = {
    "|": {(0, 1): (0, 1), (0, -1): (0, -1)},
    "-": {(1, 0): (1, 0), (-1, 0): (-1, 0)},
    "L": {(0, 1): (1, 0), (-1, 0): (0, -1)},
    "J": {(0, 1): (-1, 0), (1, 0): (0, -1)},
    "7": {(0, -1): (-1, 0), (1, 0): (0, 1)},
    "F": {(0, -1): (1, 0), (-1, 0): (0, 1)},
}

def traverse(start, points, path):
    x, y = start
    c = points[(x, y)]

    while c != "S":
        x0, y0 = path[-1]
        path.append((x, y))
        dx, dy = pipe_map[c][x - x0, y - y0]

        x, y = x + dx, y + dy
        c = points[(x, y)]

    return path

def calculate_inside(path):
    area = 0
    perimeter = len(path)
    path = path + [path[0]]

    for i in range(perimeter):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]

        area += x1 * y2 - x2 * y1
    area = abs(area // 2)

    return int(area - perimeter / 2 + 1)

with open("input.txt") as file:
    str_in = file.read().strip()

pipes = {}
for y, line in enumerate(str_in.splitlines()):
    for x, c in enumerate(line):
        if c != ".":
            pipes[x, y] = c
        if c == "S":
            start = (x, y)

path = traverse((start[0], start[1] + 1), pipes, [start])

p1 = len(path) // 2
print(p1)

p2 = calculate_inside(path)
print(p2)