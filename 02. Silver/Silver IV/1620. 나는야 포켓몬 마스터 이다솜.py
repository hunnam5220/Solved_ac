import sys

n, m = map(int, sys.stdin.readline().split())
pokemon = {}
pokemon_nm = []

for i in range(n):
    nm = sys.stdin.readline().rstrip()
    pokemon[nm] = i
    pokemon_nm.append(nm)

for _ in range(m):
    c = sys.stdin.readline().rstrip()
    if c.isnumeric():
        print(pokemon_nm[int(c) - 1])
    else:
        print(pokemon[c] + 1)
