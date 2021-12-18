from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort()
answer = []


def solve(cnt, res):
    if cnt > m:
        return

    if cnt == m:
        answer.append(res)
        return

    for i in range(cnt, n):
        if not res:
            solve(cnt + 1, res + [arr[i]])
        elif res[-1] < arr[i]:
            solve(cnt + 1, res + [arr[i]])


solve(0, [])
for i in answer:
    print(*i)
