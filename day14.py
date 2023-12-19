def value(grid):
    out = 0
    for idx, line in enumerate(grid):
        for _, v in enumerate(line):
            if v == "O":
                out += len(grid) - idx
    return out

def slide(grid):
    lines = list(map(list, grid))
    for r, row in enumerate(lines[:-1]):
        for c, col in enumerate(row):
            if col != ".":
                continue
            for south in range(r + 1, len(lines)):
                if lines[south][c] == "#":
                    break
                if lines[south][c] == "O":
                    lines[r][c] = "O"
                    lines[south][c] = "."
                    break
    return tuple(map(tuple, lines))

def rotate(grid):
    lines = list(map(list, grid))
    lines.reverse()
    lines = [[l[i] for l in lines] for i in range(len(lines))]
    return tuple(map(tuple, lines))

def cycle(grid):
    for _ in range(4):
        grid = rotate(slide(grid))
    return grid

def n_cycles(grid, n):
    map_dict = {}
    prev_maps = []
    for i in range(n):
        if grid in map_dict:
            cycle_len = i - map_dict[grid]
            pos = (n - i) % cycle_len
            pos += map_dict[grid]
            return prev_maps[pos]
        map_dict[grid] = i
        prev_maps.append(grid)
        grid = cycle(grid)
        i += 1
    return 0

with open("input.txt") as file:
    str_in = file.read().strip()

grid = tuple([tuple([i for i in j]) for j in str_in.splitlines()])

p1 = value(slide(grid))
print(p1)

p2 = value(n_cycles(grid, 1000000000))
print(p2)