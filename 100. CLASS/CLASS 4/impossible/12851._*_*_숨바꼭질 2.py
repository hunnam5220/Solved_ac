from collections import deque
from sys import stdin

n, k = map(int, stdin.readline().split())
res = []
# [만드는데 걸린 시간, 경우의 수]
dp = [[-1, 0] for _ in range(100001)]


def solve():
    q = deque()
    # 시작할 수를 저장
    q.append(n)
    # 시작하는 수에 대해 0초의 시간과 1가지의 방법이 있다고 저장
    dp[n] = [0, 1]

    # 시작과 끝이 같다면 출력하고 바로 종료
    if k == n:
        print(*dp[n], sep='\n')
        exit()

    # 큐가 빌 때까지 반복
    while q:
        x = q.popleft()

        # 이동 및 순간 이동 경우의 수
        for nx in (x - 1, x + 1, x * 2):

            # 배열 크기 넘어가면 안돼
            if -1 < nx < 100001:

                # 숫자 만들다가 그 숫자에 처음 방문하는 거라면
                if dp[nx][0] == -1:

                    # 1초 써서 만든거고
                    dp[nx][0] = dp[x][0] + 1

                    # 경우의 수는 동일하게 1개
                    dp[nx][1] = dp[x][1]

                    # 큐에 넣고 다시 반복
                    q.append(nx)

                # 숫자 만들다가 그 숫자에 처음 방문하는 거라면
                elif dp[nx][0] == dp[x][0] + 1:
                    # 경우의 수가 하나 늘어난거야
                    dp[nx][1] += dp[x][1]


solve()
print(*dp[k], sep='\n')