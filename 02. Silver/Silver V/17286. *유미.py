from sys import stdin


yumi = tuple(map(int, stdin.readline().split()))
arr = []
for i in range(3):
    pos = tuple(map(int, stdin.readline().split()))
    arr.append(pos)

arr.sort()
ans = int(1e9)
visited = set()


def solve(now, cnt, res):
    if cnt == 3:
        global ans
        ans = min(ans, res)
        return

    now_x, now_y = now
    for pos in arr:
        if pos not in visited:
            nx, ny = pos
            temp = res + (((now_x - nx) ** 2 + (now_y - ny) ** 2) ** 0.5)
            visited.add(pos)
            solve(pos, cnt + 1, temp)
            visited.discard(pos)


solve(yumi, 0, 0)
print(int(ans))