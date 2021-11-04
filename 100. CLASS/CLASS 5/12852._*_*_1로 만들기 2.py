from sys import stdin

# 1로 만들 숫자를 입력 받자
n = int(stdin.readline())

"""
# Dynamic Programming List
# n을 1로 만들면서 추적하는 것이 아니라, 1을 n으로 만들며 추적하는 방법
# 1로 만들면서 진행된 횟수와 숫자 목록를 저장할 배열을 만들어준다.
"""
dp = [[0, []] for _ in range(n + 1)]

"""
# 1을 빼고 시작하는 이유는, 다음에 계산할 나누기가 1을 뺀 값보다 작거나
# 큼에 따라 어차피 교체되기 때문이다
"""
for i in range(2, n + 1):

    # n을 만들면서 진행된 횟수
    dp[i][0] = dp[i - 1][0] + 1

    # n을 만들면서 만들어진 숫자
    dp[i][1] = dp[i - 1][1] + [i]

    if i % 2 == 0 and dp[i][0] > dp[i // 2][0] + 1:
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = dp[i // 2][1] + [i]

    if i % 3 == 0 and dp[i][0] > dp[i // 3][0] + 1:
        dp[i][0] = dp[i // 3][0] + 1
        dp[i][1] = dp[i // 3][1] + [i]

# 진행된 횟수
print(dp[n][0])

# 만들어진 숫자
print(*(list(reversed(dp[n][1])) + [1]))


"""
주석 써라 진짜
"""