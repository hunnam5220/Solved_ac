from sys import stdin

l = int(stdin.readline().rstrip())
a = int(stdin.readline().rstrip())
b = int(stdin.readline().rstrip())
c = int(stdin.readline().rstrip())
d = int(stdin.readline().rstrip())

arr = []

if a % c == 0:
    arr.append(a // c)
else:
    arr.append(a // c + 1)

if b % d == 0:
    arr.append(b // d)
else:
    arr.append(b // d + 1)

print((l - max(arr)))