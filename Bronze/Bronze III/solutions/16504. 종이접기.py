from sys import stdin

n = int(stdin.readline().rstrip())
arr = []

for step in range(n):
    arr.append(sum(list(map(int, stdin.readline().split()))))

print(sum(arr))
