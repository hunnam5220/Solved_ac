from sys import stdin

ipt = stdin.readline

a, i = ipt().rstrip().split()
print(int(a) * (int(i)-1) + 1)