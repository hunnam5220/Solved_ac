from sys import stdin

n, m = map(int, stdin.readline().split())
answer, arr = [], list(map(int, stdin.readline().split()))
arr.sort()


def solve(cnt, res):
    if cnt == m:
        answer.append(res)
        return

    for i in arr:
        solve(cnt + 1, res + [i])


solve(0, [])
for i in answer:
    print(*i)
