from sys import stdin

arr = list(map(int, stdin.readline().rstrip().split()))
x, y, r = map(int, stdin.readline().rstrip().split())
cnt = 0

for step in arr:
    if x == step:
        print(arr.index(step)+1)
        cnt += 1

if cnt == 0:
    print(0)