from sys import stdin

n = int(stdin.readline().rstrip())
arr = [1, 2]
num = 3
for step in range(n - 3):
    arr.append(num)
    num += 1

arr.append(997)

print(n)
print(' '.join(map(str, arr)))