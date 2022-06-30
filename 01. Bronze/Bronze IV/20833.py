from sys import stdin

answer = 0
for i in range(1, int(stdin.readline()) + 1):
    answer += i ** 3

print(answer)