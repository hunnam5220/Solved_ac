from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().rstrip().split())
    print('Scenario #{}:\n{}\n'.format(step + 1, (b - a + 1) * (a + b) // 2))