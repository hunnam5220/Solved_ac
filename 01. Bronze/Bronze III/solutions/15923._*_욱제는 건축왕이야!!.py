from sys import stdin

n = int(stdin.readline().rstrip())

# 처음 입력받은 x, y 좌표
x, y = map(int, stdin.readline().rstrip().split())

# 처음 입력받은 x, y 좌표 저장
sx, sy = x, y
result = 0

for step in range(1, n):
    # 지금 입력 받은 x, y 좌표
    a, b = map(int, stdin.readline().rstrip().split())

    # 계산해서 저장
    result += abs(x + y - a - b)
    x, y = a, b

# 맨처음 입력 받은 좌표값과 계산하여 결과 저장
result += abs(x + y - sx - sy)

print(result)