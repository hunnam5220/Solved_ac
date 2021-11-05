from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

a, b = stdin.readline().rstrip(), stdin.readline().rstrip()
length_a = len(a)
length_b = len(b)
lcs = [[0] * (length_b + 1) for _ in range(length_a + 1)]
ans = []

for i in range(length_a + 1):
    for j in range(length_b + 1):
        if i == 0 or j == 0:
            lcs[i][j] = 0
        elif a[i - 1] == b[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])


def solve(x, y, cost):
    if cost == 0:
        return
    if lcs[x - 1][y] == cost:
        solve(x - 1, y, cost)

    elif lcs[x][y - 1] == cost:
        solve(x, y - 1, cost)

    else:
        ans.append(a[x - 1])
        solve(x - 1, y - 1, lcs[x - 1][y - 1])


solve(length_a, length_b, lcs[length_a][length_b])
print(lcs[length_a][length_b])
if ans is not None:
    print(''.join(reversed(ans)))
