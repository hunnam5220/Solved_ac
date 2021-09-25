from sys import stdin


def solve():
    arr = set()
    n = int(stdin.readline())
    for _ in range(n):
        arr.add(stdin.readline().rstrip())

    arr = list(arr)
    for i in range(len(arr)):
        arr[i] = list(arr[i])

    arr.sort(key=lambda x: (len(x), x))

    for i in arr:
        print(''.join(i))


solve()
