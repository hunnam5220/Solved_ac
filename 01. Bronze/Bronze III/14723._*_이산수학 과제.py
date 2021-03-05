from sys import stdin

n = int(stdin.readline().rstrip())

cnt = 0
for idx in range(1, n+1):
    for jdx in range(1, idx+1):
        A = idx-jdx + 1
        B = jdx
        cnt += 1
        if cnt == n:
            print(A, B)