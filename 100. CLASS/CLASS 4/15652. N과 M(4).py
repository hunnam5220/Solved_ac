from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [x for x in range(1, n + 1)]
res = set()


def solve(l, cnt, idx):
    global res
    if cnt == m:
        res.add(tuple(l))
        return

    else:
        for i in range(n):
            if l:
                if arr[i] >= l[-1]:
                    l.append(arr[i])
                    solve(l, cnt + 1, i)
                    l.pop()
            else:
                l.append(arr[i])
                solve(l, cnt + 1, i)
                l.pop()


solve([], 0, 0)
for x in sorted(list(res)):
    print(*x)