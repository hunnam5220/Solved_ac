from sys import stdin
print(bin(int('0o' + stdin.readline().rstrip(), 8))[2:])
