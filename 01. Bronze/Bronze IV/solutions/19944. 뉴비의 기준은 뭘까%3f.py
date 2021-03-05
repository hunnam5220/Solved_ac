from sys import stdin

n, m = map(int, stdin.readline().split())

if m == 1 or m == 2:
    print('NEWBIE!')

elif n >= m > 2:
    print('OLDBIE!')

else:
    print('TLE!')