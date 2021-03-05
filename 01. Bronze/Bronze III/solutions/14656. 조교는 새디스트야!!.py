from sys import stdin

n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().rstrip().split()))

for arr_num, step in zip(arr , range(1, n+1)):
    if arr_num == step:
        n -= 1

print(n)