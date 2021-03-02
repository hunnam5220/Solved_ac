from sys import stdin

a, b, c = map(int, stdin.readline().rstrip().split())
check = False

for i in range(1, a):
    temp = a * i + b * c

    if temp ** 2 == ((a * a - b * b) * (a * a - c * c)):
        check = i

print(-1) if not check else print(check)