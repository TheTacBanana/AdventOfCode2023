import functools

with open("input.txt") as file:
    str_in = file.read()

def cards_val(f, s):
    match (f, s):
        case (5, 0): return 1
        case (4, 1): return 2
        case (3, 2): return 3
        case (3, 1): return 4
        case (2, 2): return 5
        case (2, 1): return 6
        case _:      return 7

def compare(a, b):
    if a[0] > b[0]:
        return -1
    elif a[0] < b[0]:
        return 1
    else:
        for (l, r) in zip(a[1], b[1]):
            if l < r:
                return -1
            elif r < l:
                return 1
    return 0

def make_card(s):
    cards, bid = s.split(" ")

    d = {}
    for c in cards:
        if c in d: d[c] += 1
        else: d[c] = 1

    c_vals = [*map(lambda x : "AKQJT98765432"[::-1].find(x), cards)]

    l = list(d.values()) + [0]
    l.sort(reverse=True)

    val = cards_val(l[0], l[1])
    return (val, c_vals, int(bid))

def make_card_joker(s):
    cards, bid = s.split(" ")

    d = {}
    for c in cards:
        if c in d: d[c] += 1
        else: d[c] = 1

    if "J" in d:
        keys = list(d.keys())
        if len(keys) != 1:
            keys.pop(keys.index("J"))
        maxkey = max(keys, key=d.get)

        temp = d["J"]
        d[maxkey] += temp
        d["J"] -= temp

    c_vals = [*map(lambda x : "AKQT98765432J"[::-1].find(x), cards)]

    l = list(d.values()) + [0]
    l.sort(reverse=True)

    val = cards_val(l[0], l[1])
    return (val, c_vals, int(bid))

# Part 1

cards_out = [*map(make_card, str_in.splitlines())]
cards_out.sort(key=functools.cmp_to_key(compare))
print(sum([*map(lambda x : (x[0] + 1) * x[1][2], enumerate(cards_out))]))

# Part 2

cards_out = [*map(make_card_joker, str_in.splitlines())]
cards_out.sort(key=functools.cmp_to_key(compare))
print(sum([*map(lambda x : (x[0] + 1) * x[1][2], enumerate(cards_out))]))