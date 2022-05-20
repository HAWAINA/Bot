def seishely(d):
    if 3 < d < 7:
        return (d * 40) - 20
    elif d >= 7:
        return (d * 40) - 50
    return d * 40


d_1 = 1
d_2 = 4
print(seishely(7))
