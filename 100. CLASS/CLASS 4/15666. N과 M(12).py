from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

res = set()
n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))


def dfs(r, brr, cnt):
    if cnt == m and tuple(r) not in res:
        res.add(tuple(r))
        return
    elif cnt > m:
        return
    else:
        for i in range(len(brr)):
            if r:
                if r[-1] <= brr[i]:
                    r.append(brr[i])
                    dfs(r, brr, cnt + 1)
                    r.pop()
            else:
                r.append(brr[i])
                dfs(r, brr, cnt + 1)
                r.pop()


dfs([], arr, 0)
for i in sorted(list(res)):
    print(*i)