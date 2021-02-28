from sys import stdin

a, m = map(int, stdin.readline().rstrip().split())
result = 1

while 1:
    if (a * result) % m == 1:
        print(result)
        break
    else:
        result += 1