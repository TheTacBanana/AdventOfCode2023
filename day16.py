from enum import Enum

class Dir(Enum):
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

    def offset_from(self, pos):
        x, y = self.value
        return (x + pos[0], y + pos[1])

    def reflect(self, mirror):
        if mirror == "/":
            match self:
                case self.NORTH:
                    return Dir.EAST
                case self.EAST:
                    return Dir.NORTH
                case self.SOUTH:
                    return Dir.WEST
                case self.WEST:
                    return Dir.SOUTH
        elif mirror == "\\":
            match self:
                case self.NORTH:
                    return Dir.WEST
                case self.EAST:
                    return Dir.SOUTH
                case self.SOUTH:
                    return Dir.EAST
                case self.WEST:
                    return Dir.NORTH

    def split(self, splitter):
        if splitter == "|":
            match self:
                case self.NORTH:
                    return [Dir.NORTH]
                case self.EAST:
                    return [Dir.NORTH, Dir.SOUTH]
                case self.SOUTH:
                    return [Dir.SOUTH]
                case self.WEST:
                    return [Dir.NORTH, Dir.SOUTH]
        elif splitter == "-":
            match self:
                case self.NORTH:
                    return [Dir.EAST, Dir.WEST]
                case self.EAST:
                    return [Dir.EAST]
                case self.SOUTH:
                    return [Dir.EAST, Dir.WEST]
                case self.WEST:
                    return [Dir.WEST]

def calc_energized(grid, start_beam):
    visited = set()
    beams = [start_beam]
    while len(beams):
        pos, dir = beams.pop(0)
        if (pos, dir) in visited:
            continue
        new_pos = dir.offset_from(pos)

        if (pos[0] >= 0 and pos[1] >= 0 and
           pos[0] < len(grid[0]) and pos[1] < len(grid)):
            visited.add((pos, dir))

        if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= len(grid[0]) or new_pos[1] >= len(grid):
            continue

        grid_char = grid[new_pos[1]][new_pos[0]]

        match grid_char:
            case ".":
                beams.append((new_pos, dir))
            case "/" | "\\":
                new_dir = dir.reflect(grid_char)
                beams.append((new_pos, new_dir))
            case "|" | "-":
                new_dirs = dir.split(grid_char)
                beams.extend([(new_pos, i) for i in new_dirs])

    visited = {i[0] for i in visited}
    return len(visited)

with open("input.txt") as file:
    str_in = file.readlines()

grid = [[j for j in i.strip()] for i in str_in]

p1 = calc_energized(grid, ((-1,0),Dir.EAST))
print(p1)

all_starts = (
    [((i, -1), Dir.SOUTH) for i in range(len(grid[0]))] +
    [((i, len(grid)), Dir.NORTH) for i in range(len(grid[0]))] +
    [((-1, i), Dir.EAST) for i in range(len(grid))] +
    [((len(grid[0]), i), Dir.WEST) for i in range(len(grid))]
    )

p2 = max([calc_energized(grid, start) for start in all_starts])
print(p2)