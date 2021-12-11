from sys import stdin
from itertools import combinations

n = int(stdin.readline())
ability = [[0] * (n + 1) for _ in range(n + 1)]
teams = [x for x in range(1, n + 1)]
for i in range(1, n + 1):
    data = list(map(int, stdin.readline().split()))
    for j in range(1, n + 1):
        ability[i][j] = data[j - 1]

ans = int(1e9)
for i in range(1, n):
    for team in list(set(combinations(teams, i))):
        link = team
        start = list(set(teams) - set(link))

        link_point = 0
        if i != 0:
            for j in range(i):
                for k in range(j + 1, i):
                    link_point += ability[link[j]][link[k]]
                    link_point += ability[link[k]][link[j]]

        start_point = 0
        if n - i != 1:
            for j in range(n - i):
                for k in range(j + 1, n - i):
                    start_point += ability[start[j]][start[k]]
                    start_point += ability[start[k]][start[j]]

        ans = min(ans, abs(start_point - link_point))
        if ans == 0:
            break

print(ans)