from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

n, m = map(int, stdin.readline().split())
arr = [x for x in range(1, n + 1)]
res = set()


def solve(brr, cnt):
    if cnt == m:
        res.add(tuple(brr))
        return

    else:
        for i in arr:
            solve([i]+brr, cnt + 1)
    return


solve([], 0)
res = list(res)
res.sort()
for i in res:
    print(*i)