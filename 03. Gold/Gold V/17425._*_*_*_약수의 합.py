from sys import stdin
# 최대값 설정
MAX = int(1e6)

# DP 1로 초기화
dp = [1]*(MAX+1)

# S: 값 누적 리스트
s = [0]*(MAX+1)

for i in range(2, MAX+1):
    j=1
    # i가 N의 약수일 때, i의 배수가 N보다 작다면
    # i의 배수는 N의 약수이다.
    while i*j <= MAX:

        # i의 배수에 값 추가
        dp[i*j] += i
        j += 1

for i in range(1, MAX+1):
    # 누적 값 계산
    s[i] = s[i-1] + dp[i]

for _ in range(int(stdin.readline())):
    print(s[int(stdin.readline())])