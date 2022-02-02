from sys import stdin

a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
n = int(stdin.readline())

for _ in range(17, n + 1):
    a.append((a[-2] + a[-1]) % 1000000007)

print(a[n])