with open("input.txt") as file:
    str_in = file.read().strip()

def search(inst):
    cur_pos = (0, 0)
    all_pos = [cur_pos]
    for (n, dir) in inst:
        match dir:
            case "U":
                dir = (0, -1)
            case "R":
                dir = (1, 0)
            case "D":
                dir = (0, 1)
            case "L":
                dir = (-1, 0)
        x, y = cur_pos
        dir_x, dir_y = dir
        new_pos = (x + (dir_x * n), y + (dir_y * n))
        all_pos.append(new_pos)
        cur_pos = new_pos

    border = 2
    s = 0
    for ((x0, y0), (x1, y1)) in zip(all_pos, all_pos[1:] + [all_pos[0]]):
        s += x0*y1 - x1*y0
        border += abs(x0 - x1) + abs(y0 - y1)
    a = abs(s)
    return int(0.5 * (a + border))

p1_in = [*map(lambda x : (int((y := x.split(" "))[1]), y[0]), str_in.splitlines())]
p1 = search(p1_in)
print(p1)

p2_in = [*map(lambda x : (int((y := x.split(" ")[2][2:-1])[:-1], 16), ("R","D","L","U")[int(y[-1])]), str_in.splitlines())]
p2 = search(p2_in)
print(p2)