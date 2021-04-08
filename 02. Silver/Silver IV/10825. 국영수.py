from sys import stdin

arr = []
for step in range(int(stdin.readline().rstrip())):
    arr.append(list(stdin.readline().rstrip().split()))

arr.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for step in arr:
    print(step[0])