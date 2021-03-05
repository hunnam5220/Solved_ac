from sys import stdin

n = int(stdin.readline().rstrip())

stars = 1
for step in range(0, n):
    print(' ' * (n - (step + 1)) + '*' * stars)
    stars += 2
