from math import ceil, floor, sqrt

with open("input.txt") as file:
    str_in = file.read()

lines = str_in.splitlines()
times = [int(i) for i in lines[0].split(" ")[1:] if i != ""]
records = [int(i) for i in lines[1].split(" ")[1:] if i != ""]

def calc(t, r):
    h1 = 1 / 2 * (t - sqrt(t**2 - 4 * r))
    h2 = 1 / 2 * (t + sqrt(t**2 - 4 * r))
    nways = floor(h2) - ceil(h1) + 1
    return nways

product = 1
for (t, r) in zip(times, records):
    product *= calc(t, r)
print(product)

t = int("".join(str(i) for i in times))
r = int("".join(str(i) for i in  records))

print(calc(t, r))