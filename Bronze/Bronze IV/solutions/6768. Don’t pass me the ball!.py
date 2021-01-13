from sys import stdin
import math

n = int(stdin.readline().rstrip())

if n < 4:
    print(0)

else:
    # 90번 을 입력했을 때, 90번 플레이어가 골을 넣어야하므로, n-1, 즉 89에 대해 계산.
    print(int(math.factorial(n - 1) / (math.factorial(n - 1 - 3) * math.factorial(3))))
