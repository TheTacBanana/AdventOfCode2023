import numpy as np

def find(grid, smudge=False):
    for row in range(1, grid.shape[0]):
        rhs = grid[row:row + row:]
        lhs = grid[row-rhs.shape[0]:row:]
        if smudge:
            if np.sum(lhs != np.flip(rhs, axis=0)) == 1:
                return row
        elif np.array_equal(lhs, np.flip(rhs, axis=0)):
            return row
    return 0

with open("input.txt") as file:
    str_in = file.read()

patterns = [s for s in str_in.split("\n\n")]
patterns = [np.array([[c=="#" for c in r] for r in pat.splitlines()]) for pat in patterns]

s = [100 * find(pat) + find(pat.T) for pat in patterns]
print(sum(s))

s = [100 * find(pat, True) + find(pat.T, True) for pat in patterns]
print(sum(s))