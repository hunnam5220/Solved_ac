from sys import stdin
a = [1] + [0 for _ in range(42)]
a[2] = 1
for i in range(3, 42):
    a[i] = a[i-2] + a[i-1]

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    print(a[n], a[n + 1])