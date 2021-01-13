from sys import stdin

arr = []
for x in range(5):
    y = int(stdin.readline().rstrip())
    if y < 40:
        y = 40
    arr.append(y)

print(int(sum(arr) / 5))