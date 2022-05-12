from sys import stdin

arr = []
visited = [1 for _ in range(9)]

for _ in range(9):
    arr.append(int(stdin.readline()))


def solve(cnt, res):
    if cnt == 7:
        if sum(res) == 100:
            res.sort()
            print(*res, sep='\n')
            exit()

        return

    for i in range(9):
        if visited[i] == 1:
            res.append(arr[i])
            visited[i] = 0

            solve(cnt + 1, res)

            visited[i] = 1
            res.pop()


solve(0, [])