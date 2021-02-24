from sys import stdin

t = int(stdin.readline().rstrip())
result = ''

for step in range(4, -1, -1):
    n = t // (9 ** step)
    result += str(n)
    t = t - (n * (9 ** step))

print(int(result))