from sys import stdin

n = int(stdin.readline().rstrip())

stars = 1
for step in range(0, n):
    print(' ' * (n - (step + 1)) + '*' * stars)
    stars += 2

stars -= 4

for step in reversed(range(n+1)):
    print(' ' * (n+1 - step) + '*' * stars)
    stars -= 2