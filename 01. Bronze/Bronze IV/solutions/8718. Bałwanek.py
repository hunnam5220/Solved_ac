from sys import stdin

n, k = map(int, stdin.readline().rstrip().split())

arr = []

while True:
    chk = [k, k / 2, k / 2 / 2]

    if sum(chk) < n:
        arr = chk
        k *= 2
    elif sum(chk) == n:
        print(int(sum(chk)) * 1000)
        break
    else:
        print(int(sum(arr) * 1000))
        break