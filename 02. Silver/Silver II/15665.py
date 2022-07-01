from sys import stdin

n, m = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
answer = set()


def dfs(cnt, stat):
    if cnt == m:
        answer.add(tuple(stat))
        return

    for i in range(n):
        stat.append(nums[i])
        dfs(cnt + 1, stat)
        stat.pop()


dfs(0, [])

for ans in sorted(list(answer)):
    print(*ans)