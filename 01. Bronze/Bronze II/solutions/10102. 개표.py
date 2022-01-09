from sys import stdin
n = int(stdin.readline())
s = stdin.readline().rstrip()
a, b = s.count('A'), s.count('B')
if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')