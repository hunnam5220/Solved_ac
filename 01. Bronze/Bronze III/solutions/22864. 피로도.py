from sys import stdin

a, b, c, d = map(int, stdin.readline().split())
stamina = d
work = 0

for i in range(24):
    if stamina - a < 0:
        stamina = stamina + c if stamina + c <= d else d

    else:
        stamina -= a
        work += b

print(work)