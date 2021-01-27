from sys import stdin

n = int(stdin.readline().rstrip())

stars = 1
for step in range(n-1):
    stars += 2

for step in reversed(range(n+1)):
    print(' ' * (n - step) + '*' * stars)
    stars -= 2
