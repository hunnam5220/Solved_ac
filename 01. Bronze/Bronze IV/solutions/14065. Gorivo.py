from sys import stdin
x = float(stdin.readline().rstrip())

l = 3.785411784
km = 1.609344

print((100 / (km * x)) * l)