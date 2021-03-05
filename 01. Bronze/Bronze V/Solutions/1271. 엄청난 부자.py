from sys import stdin

ipt = stdin.readline

n, m = ipt().rstrip().split()
n, m = int(n), int(m)

print(n // m)
print(n % m)