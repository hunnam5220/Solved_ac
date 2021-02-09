from sys import stdin

t = int(stdin.readline().rstrip())

for step in range(t):
    arr = sorted(list(map(int, stdin.readline().rstrip().split())))

    if sum(arr[:2]) <= arr[-1]:
        print('Case #{}: invalid!'.format(step + 1))

    else:
        n = len(set(arr))
        if n == 1:
            print('Case #{}: equilateral'.format(step + 1))

        elif n == 2:
            print('Case #{}: isosceles'.format(step + 1))

        else:
            print('Case #{}: scalene'.format(step + 1))