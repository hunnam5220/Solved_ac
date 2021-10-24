"""
카데인 알고리즘 적
"""

from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [[0] * (m + 1)]
for _ in range(n):
    arr.append([0] + list(map(int, stdin.readline().split())))

ans = -int(4e9) - 1

# 열단위 더한 값을 psum 2차원 리스트에 저장
psum = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        psum[i][j] = arr[i][j] + psum[i - 1][j]


for i in range(1, n + 1):
    for j in range(i, n + 1):
        # i행부터 j행까지 더해준 값을 최대 연속합 구해서 비교해줄 것이다.
        dp = [0] * (m + 1)

        for k in range(1, m + 1):
            # i~j의 행을 더한 값(k로만 이루어진 원소값) vs 최대 연속 합
            dp[k] = max(psum[j][k] - psum[i - 1][k], dp[k - 1] + psum[j][k] - psum[i - 1][k])
            ans = max(dp[k], ans)
print(ans)
