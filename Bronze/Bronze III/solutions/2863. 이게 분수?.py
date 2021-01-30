from sys import stdin

arr = []

for step in range(2):
    arr.append(list(map(int, stdin.readline().rstrip().split())))

m = []
for step in range(4):
    m.append((arr[0][0] / arr[1][0]) + (arr[0][1] / arr[1][1]))

    tmp = arr[1][0]
    arr[1][0] = arr[1][1]
    arr[1][1] = arr[0][1]
    arr[0][1] = arr[0][0]
    arr[0][0] = tmp

print(m.index(max(m)))