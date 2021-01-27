from sys import stdin

n = int(stdin.readline().rstrip())

stars = n * 2 - 1

for step in reversed(range(1, n+1)):
    print(' ' * (n - step) + '*' * stars)
    stars -= 2

stars = 3
for step in range(0, n-1):
    print(' ' * (n - (step + 2)) + '*' * stars)
    stars += 2