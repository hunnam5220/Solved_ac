from sys import stdin

n = int(stdin.readline().rstrip())

# 지수표기법을 사용하지 않고 소수점 출력하는 법
print("%.{}f".format(n) % pow(2, -1 * n))