from sys import stdin

arr = []
n = int(stdin.readline())
for i in range(n):
    arr.append(list(map(int, stdin.readline().split())))

arr.sort(key= lambda x: (x[0], x[1]))

for i in arr:
    print(*i)