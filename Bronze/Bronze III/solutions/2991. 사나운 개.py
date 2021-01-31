from sys import stdin

a, b, c, d = map(int, stdin.readline().split())
p, m, n = map(int, stdin.readline().split())

fd = []
sd = []

for step in range(max(p, m, n) // min([a, b, c, d])):
    fd.extend([True] * a)
    fd.extend([False] * b)

    sd.extend([True] * c)
    sd.extend([False] * d)

for step in [p, m, n]:
    result = 0
    if fd[step-1]:
        result += 1
    if sd[step-1]:
        result += 1

    print(result)