from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
res = set()


def solve(brr, l, idx):
    if l == m:
        res.add(tuple(brr))
        return
    else:
        for i in range(n):
            if arr[i] not in brr:
                brr.append(arr[i])
                solve(brr, l + 1, i)
                brr.pop()


solve([], 0, 0)
for x in sorted(list(res)):
    print(*x)