from sys import stdin

n, r = map(int, stdin.readline().rstrip().split())
arr = list(map(int, stdin.readline().split()))
result = []
for i in range(1, n + 1):
    if i not in arr:
        result.append(i)

if result:
    for i in result:
        print(i, end=" ")
    print()
else:
    print('*')
