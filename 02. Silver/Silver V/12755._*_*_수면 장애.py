from sys import stdin

n = int(stdin.readline())
l, idx, s = 1, 1, ''
while 1:
    if idx * 9 * l < n:
        n -= idx * 9 * l
        idx *= 10
        l += 1
    else:
        break


temp_a, temp_b = n // l, n % l

idx += temp_a

if temp_b == 0:
    print(str(idx - 1)[-1])
else:
    print(str(idx)[temp_b - 1])