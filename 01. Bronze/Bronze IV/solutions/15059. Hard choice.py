from sys import stdin

supply = list(map(int, stdin.readline().split()))
demand = list(map(int, stdin.readline().split()))
result = [0 for _ in range(len(supply))]

for i in range(len(supply)):
    if supply[i] >= demand[i]:
        result[i] = 0
    else:
        result[i] = demand[i] - supply[i]

print(sum(result))
