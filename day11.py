with open("input.txt") as file:
    str_in = file.read()

def find(grid, space):
    width = len(grid)
    height = len(grid)

    galaxies = {}

    for (r, row) in enumerate(grid):
        for (c, col) in enumerate(row):
            if col == "#":
                galaxies[(r, c)] = []

    empty_rows = [not sum([1 for i in row if i == "#"]) for row in grid]
    empty_cols = [not sum([1 for row in range(height) if grid[row][col] == "#"]) for col in range(width)]

    pairs = set()
    for (r1, c1) in galaxies:
        for (r2, c2) in galaxies:
            if r1 == r2 and c1 == c2:
                continue
            if (r1, c1, r2, c2) in pairs or (r2, c2, r1, c1) in pairs:
                continue

            emptyrows = 0
            for row in range(min(r1, r2), max(r1, r2) + 1):
                if empty_rows[row]:
                    emptyrows += 1

            emptycols = 0
            for col in range(min(c1, c2), max(c1, c2) + 1):
                if empty_cols[col]:
                    emptycols += 1

            both = emptyrows + emptycols
            galaxies[(r1, c1)].append(abs(c1 - c2) + abs(r1 - r2) - both + (both * space))
            pairs.add((r1, c1, r2, c2))

    return sum(map(sum, galaxies.values()))

grid = [[i for i in j] for j in str_in.splitlines()]

p1 = find(grid, 2)
print(p1)

p2 = find(grid, 1000000)
print(p2)