from sys import stdin

res = set()
n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))


def dfs(r, brr, cnt):
    if cnt == m and tuple(r) not in res:
        res.add(tuple(r))
        return
    else:
        for i in range(len(brr)):
            r.append(brr[i])
            temp = brr[:]
            temp.pop(i)
            dfs(r, temp, cnt + 1)
            r.pop()


dfs([], arr, 0)
for i in sorted(list(res)):
    print(*i)