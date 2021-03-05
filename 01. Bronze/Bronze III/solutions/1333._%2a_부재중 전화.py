from sys import stdin

n, l, d = map(int, stdin.readline().split())

music = []
idx = d
for x in range(n):
    music += [False] * l
    if n-1 != x:
        music += [True] * 5
    else:
        break

try:
    while True:
        if music[idx] is not True:
            idx += d
        else:
            print(idx)
            break
except:
    print(idx)