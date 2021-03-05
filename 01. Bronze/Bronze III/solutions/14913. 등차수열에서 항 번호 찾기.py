from sys import stdin

a, d, k = map(int, stdin.readline().split())
n = 1
while 1:
    if a == k:
        print(n)
        break
    else:
        a += d
        n += 1

    if d > 0:
        if a > k:
            print('X')
            break

    else:
        if a < k:
            print('X')
            break