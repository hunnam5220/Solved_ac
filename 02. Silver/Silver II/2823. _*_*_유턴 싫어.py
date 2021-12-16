from collections import deque
from sys import stdin

r, c = map(int, stdin.readline().split())
arr, roads, dx, dy = [], [], [1, 0, 0, -1], [0, 1, -1, 0]

# row의 개수만큼 데이터를 입력받아 arr에 저장
for i in range(r):
    data = list(stdin.readline().rstrip())
    arr.append(data)

    # .에 해당되는 좌표를 길인지 아닌지 구별해 roads에 저장
    for j in range(c):
        if data[j] == '.':
            roads.append((i, j))


def solve(x, y):
    q = deque()
    q.append((x, y))
    visited = set()

    while q:
        x, y = q.popleft()
        # . 하나당 길이 두 개 이상 있어야 한다.
        # 그 조건을 알아낼 수 있는 cnt를 만든다.
        cnt = 0

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if -1 < nx < r and -1 < ny < c:
                if arr[nx][ny] == '.':
                    cnt += 1

                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny))

        # 길이 두개 이하라면 1을 return
        if cnt < 2:
            return 1

    return 0


for x, y in roads:
    # 유턴을 하지 않고 제자리로 돌아올 수 있다면
    # 0 출력하고 종료
    if solve(x, y) == 0:
        print(0)
        exit()
print(1)