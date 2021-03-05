from sys import stdin

l, r, a = map(int, stdin.readline().rstrip().split())
cnt = 0


for step in range(a):
    if l > r:
        r += 1
    else:
        l += 1

if r <= l:
    print(r * 2)
elif r > l:
    print(l * 2)