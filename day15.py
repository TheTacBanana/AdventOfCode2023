with open("input.txt") as file:
    str_in = file.read().strip()

def hash(string):
    val = 0
    for c in string:
        val += ord(c)
        val *= 17
        val %= 256
    return val

sequence = str_in.split(",")
p1 = 0
for p2 in sequence:
    p1 += hash(p2)
print(p1)

sequence = str_in.split(",")
boxes = [[] for i in range(256)]
for p2 in sequence:
    if "=" in p2:
        lhs, rhs = p2.split("=")
        h = hash(lhs)
        box = boxes[h]
        for (i, (k, v)) in enumerate(box):
            if k == lhs:
                box[i] = (lhs,rhs)
                break
        else:
            box.append((lhs, rhs))
    elif "-" in p2:
        lhs, rhs = p2.split("-")
        h = hash(lhs)
        box = boxes[h]
        for (i, (k, v)) in enumerate(box):
            if k == lhs:
                box.pop(i)
                break

p2 = 0
for (b_i, b) in enumerate(boxes):
    for (i, (k, v)) in enumerate(b):
        val = (int(b_i) + 1) * (i + 1) * int(v)
        p2 += val
print(p2)