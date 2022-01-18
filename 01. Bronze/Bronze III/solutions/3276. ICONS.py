from sys import stdin

a, b = 1, 1
n = int(stdin.readline())

while a * b < n:
    if a <= b:
        a += 1
    else:
        b += 1

print(a, b)