from sys import stdin

start = list(map(int, stdin.readline().rstrip().split()))
end = list(map(int, stdin.readline().rstrip().split()))
num = int(stdin.readline().rstrip())
result = 0

while 1:
    if start[0] % 10 == num or start[1] % 10 == num or start[0] // 10 == num or start[1] // 10 == num:
        result += 1

    if start == end:
        break

    start[1] += 1

    if start[1] == 60:
        start[1] = 0
        start[0] += 1

print(result)