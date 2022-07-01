from sys import stdin

l = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
n = int(stdin.readline())
arr.append(0)
arr.sort()
section = []

for i in range(n):
    if arr[i] <= n <= arr[i + 1]:
        section = (arr[i] + 1, arr[i + 1] - 1)
        break

answer = set()

for i in range(section[0], section[1] + 1):
    for j in range(i + 1, section[1] + 1):
        if i <= n <= j:
            answer.add((i, j))

print(len(answer))