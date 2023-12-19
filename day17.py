from heapq import *

NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)

def search(grid, start, target, min_steps, max_steps):
    height = len(grid)
    width = len(grid[0])

    queue = []
    visited = set()

    heappush(queue, (0, start, *EAST, 0))
    heappush(queue, (0, start, *SOUTH, 0))
    while queue:
        loss, position, dirx, diry, cur_steps = heappop(queue)
        dir = (dirx, diry)
        x, y = position

        if (position, dir, cur_steps) in visited:
            continue

        if position == target and cur_steps >= min_steps:
            return loss

        visited.add((position, dir, cur_steps))

        if cur_steps >= min_steps:
            if dir in (EAST, WEST):
                if y+1 < height:
                    heappush(queue, (loss + grid[y+1][x], (x, y+1), *SOUTH, 1))
                if y-1 >= 0:
                    heappush(queue, (loss + grid[y-1][x], (x, y-1), *NORTH, 1))
            if dir in (NORTH, SOUTH):
                if x+1 < width:
                    heappush(queue, (loss + grid[y][x+1], (x+1, y), *EAST, 1))
                if x-1 >= 0:
                    heappush(queue, (loss + grid[y][x-1], (x-1, y), *WEST, 1))

        if cur_steps < max_steps:
            x, y = x + dir[0], y + dir[1]
            if 0 <= x < width and 0 <= y < height:
                heappush(queue, (loss + grid[y][x], (x, y), *dir, cur_steps+1))

with open("input.txt") as file:
    str_in = file.read().strip()

grid = [[int(i) for i in j] for j in str_in.splitlines()]

p1 = search(grid, (0,0), (len(grid[0])-1, len(grid)-1), 0, 3)
print(p1)

p2 = search(grid, (0,0), (len(grid[0])-1, len(grid)-1), 4, 10)
print(p2)