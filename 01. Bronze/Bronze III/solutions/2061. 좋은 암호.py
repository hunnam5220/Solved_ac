from sys import stdin


def bad_or_good(k, l):
    for step in range(2, l):
        if k % step == 0:
            return 'BAD {}'.format(step)
    return 'GOOD'


k, l = map(int, stdin.readline().rstrip().split())
print(bad_or_good(k, l))