from sys import stdin


def sol1(k1, o1, k2, o2, k3):
    if o1 == '/':
        if (int(k1) < 0 and int(k2) > 0) or (int(k1) > 0 and int(k2) < 0):
            r1 = abs(int(k1)) // abs(int(k2)) * -1
        else:
            r1 = int(k1) // int(k2)
    else:
        r1 = eval(k1 + o1 + k2)

    if o2 == '/':
        if (r1 < 0 and int(k3) > 0) or (r1 > 0 and int(k3) < 0):
            r2 = abs(r1) // abs(int(k3)) * -1
        else:
            r2 = r1 // int(k3)
    else:
        r2 = eval(str(r1) + o2 + k3)

    return r2


def sol2(k1, o1, k2, o2, k3):
    if o2 == '/':
        if (int(k2) < 0 and int(k3) > 0) or (int(k2) > 0 and int(k3) < 0):
            r1 = abs(int(k2)) // abs(int(k3)) * -1
        else:
            r1 = int(k2) // int(k3)
    else:
        r1 = eval(k2 + o2 + k3)

    if o1 == '/':
        if (r1 < 0 and int(k1) > 0) or (r1 > 0 and int(k1) < 0):
            r2 = abs(int(k1)) // abs(r1)  * -1
        else:
            r2 = int(k1) // r1
    else:
        r2 = eval(k1 + o1 + str(r1))

    return r2


k1, o1, k2, o2, k3 = list(stdin.readline().rstrip().split())
a = sol1(k1, o1, k2, o2, k3)
b = sol2(k1, o1, k2, o2, k3)

print(min([a, b]))
print(max([a, b]))