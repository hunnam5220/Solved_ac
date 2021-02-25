from sys import stdin

n = int(stdin.readline().rstrip())

a = 1
k = 1

while 1:
    if a + a * k + a * k * k == n:
        print(k)
        break
    else:
        k += 1