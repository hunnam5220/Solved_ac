from sys import stdin

arr = list(map(int, stdin.readline().rstrip().split()))

if (arr[0]-arr[1]) < 0 or (arr[0]-arr[1]) % 2 != 0:
    print(-1)
else:
    result = [int((arr[0]+arr[1])/2), int((arr[0]-arr[1])/2)]
    print(max(result), min(result))