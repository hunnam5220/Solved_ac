from sys import stdin

arr = []

for x in range(5):
    arr.append(int(stdin.readline().rstrip()))

x = arr[0] * arr[-1]
y = arr[1]
plus_cost = 0

if arr[2] < arr[-1]:
    plus_cost = arr[-1] - arr[2]
    y += plus_cost * arr[3]

if x > y:
    print(y)
else:
    print(x)
