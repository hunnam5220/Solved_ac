from sys import stdin

# 12시간동안 abs(a / b - 1) 회 만난다.
# 24시간은 * 2를 하고 정수 부분을 취해주면 된다.
a, b = map(int, stdin.readline().rstrip().split())
print('%d' % (abs(a / b - 1) * 2))