from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
res = set()


def solve(brr, l):
    if l == m:
        res.add(tuple(brr))
        return
    else:
        for i in range(n):
            if brr:
                if brr[-1] <= arr[i]:
                    brr.append(arr[i])
                    solve(brr, l + 1)
                    brr.pop()
            else:
                brr.append(arr[i])
                solve(brr, l + 1)
                brr.pop()


solve([], 0)
for x in sorted(list(res)):
    print(*x)