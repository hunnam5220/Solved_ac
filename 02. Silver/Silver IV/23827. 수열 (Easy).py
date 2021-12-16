from sys import stdin
"""
1. 수열이 주어졌을 때, 수열의 합을 먼저 구하고
2. 수열을 순회하면서 방문하고 있는 수열의 값을 수열의 합에서 빼준 뒤
3. 방문하고 있는 수열에 곱하여 반환하려는 변수 값에 더 해준다.

[a, b, c] 수열이 있다면, a * b + a * c + b * c 가 정답인데,
a 를 기준으로 곱할 수 있는 겹치지 않는 경우의 수를 본다면 ab + ac 가 있을 것이다.
결합법칙으로 인해 a * (b + c) 이다. 이는 수열의 총합인 (a + b + c) 에서 a를 빼준 값에서 a를 곱해준 것.

출력하고자 하는 값에서 1000000007로 나눈 나머지를 출력한다.
"""
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
r = 0
s = sum(a)
for i in range(n):
    r += a[i] * (s - a[i])

print((r // 2) % 1000000007)