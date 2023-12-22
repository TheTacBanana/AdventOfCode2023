import numpy
from math import isnan
from typing import DefaultDict

with open("input.txt") as file:
    str_in = file.read().strip()

class Brick():
    def __init__(self, fr, to):
        self.points = set()
        self.fr = fr
        self.to = to

        dir = to - fr
        mag = numpy.linalg.norm(dir)
        dir = dir / mag
        if isnan(dir[0]):
            self.points.add((int(self.fr[0]), int(self.fr[1]), int(self.fr[2])))
        else:
            for i in range(int(mag) + 1):
                point = self.fr + dir * i
                self.points.add((int(point[0]), int(point[1]), int(point[2])))

    def min_point_z(self):
        return min(self.fr[2], self.to[2])

    def intersect_with_brick(self, other):
        i = self.points.intersection(other.points)
        return len(i) > 0

    def brick_minus(self):
        n_fr = numpy.array(self.fr, copy=True)
        n_fr[2] -= 1
        n_to = numpy.array(self.to, copy=True)
        n_to[2] -= 1
        return Brick(n_fr, n_to)

bricks = []
for line in str_in.splitlines():
    bricks.append(Brick(*[numpy.array([int(j) for j in i.split(",")]) for i in line.split("~")]))
bricks.sort(key=lambda x : x.min_point_z())

bricks_on = DefaultDict(list)
bricks_supporting = DefaultDict(list)
solid = []
while len(bricks):
    brick_list = [bricks.pop(0)]
    while True:
        intersections = []
        for bi, brick in enumerate(solid):
            if brick.intersect_with_brick(brick_list[-1]):
                intersections.append(bi)

        if len(intersections):
            ni = len(solid)
            for i in intersections:
                bricks_supporting[i].append(ni)
            bricks_on[ni] = intersections
            solid.append(brick_list[-2])
            break

        brick_list.append(brick_list[-1].brick_minus())
        if brick_list[-1].min_point_z() == 0:
            solid.append(brick_list[-2])
            break

p1 = 0
for i in range(len(solid)):
    destroy = True
    for supported in bricks_supporting[i]:
        if len(bricks_on[supported]) == 1:
            destroy = False
    if destroy:
        p1 += 1
print(p1)

def traverse(i, destroyed):
    next = []
    for supported in bricks_supporting[i]:
        if len([s for s in bricks_on[supported] if s not in destroyed]) == 0:
            destroyed.add(supported)
            next.append(supported)
    for i in next:
        traverse(i, destroyed)
    return destroyed

p2 = sum([len(traverse(i, {i})) - 1 for i in range(len(solid))])
print(p2)

# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# for b in solid:
#     ax.plot([b.fr[0], b.to[0]],[b.fr[1], b.to[1]],[b.fr[2], b.to[2]])
# plt.show()
# Axes3D.plot()