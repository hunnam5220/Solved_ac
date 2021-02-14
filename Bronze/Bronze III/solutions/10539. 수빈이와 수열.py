from sys import stdin

n = int(stdin.readline().rstrip())


if n == 1:
    print(int(stdin.readline().rstrip()))

else:
    arr = list(map(int, stdin.readline().rstrip().split()))
    result = [arr[0]]
    for step in range(2, n+1):
        result.append(arr[step-1] * step - sum(result[:step]))
    print(' '.join(map(str, result)))