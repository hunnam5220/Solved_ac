from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
city = []
for x in range(n):
    city.append(list(map(int, stdin.readline().split())))

bbq = []
house = []
result = int(1e9)


def check(k, house):
    result = []
    for x1, y1 in house:
        tmp = []
        for x2, y2 in k:
            tmp.append(abs(x1 - x2) + abs(y1 - y2))

        result.append(min(tmp))

    return sum(result)


for x in range(n):
    for y in range(n):
        if city[x][y] == 1:
            house.append([x + 1, y + 1])
        if city[x][y] == 2:
            bbq.append([x + 1, y + 1])

bbq_comb = list(combinations(bbq, m))

for k in bbq_comb:
    tmp = check(k, house)
    if result > tmp:
        result = tmp

print(result)