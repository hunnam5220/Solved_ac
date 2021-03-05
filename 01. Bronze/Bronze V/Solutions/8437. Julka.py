from sys import stdin
n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())

s = (n-m) // 2
print(s + m)
print(s)