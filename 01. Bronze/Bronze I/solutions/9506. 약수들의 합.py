from sys import stdin

while 1:
    arr = [1]
    n = int(stdin.readline())
    if n == -1:
        break

    for i in range(2, n // 2):
        if n % i == 0 and i not in arr:
            arr.append(i)
            arr.append(n // i)

    arr.sort()

    if sum(arr) == n:
        print('{} = '.format(n), end='')
        for i in range(len(arr) - 1):
            print('{} + '.format(arr[i]), end='')
        print('{}'.format(arr[-1]))

    else:
        print(n, 'is NOT perfect.')