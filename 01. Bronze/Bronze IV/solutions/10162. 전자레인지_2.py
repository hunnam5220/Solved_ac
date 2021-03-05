from sys import stdin

arr = []
for x in range(5):
    arr.append(int(stdin.readline().rstrip()))

result = 0
if arr[0] < 0:
    result = (abs(arr[0]) * arr[2]) + arr[3] + (arr[1] * arr[4])

elif arr[0] == 0:
    result = arr[3] + arr[1] * arr[4]

elif arr[0] > 0:
    result = abs(arr[0]-arr[1]) * arr[4]

print(result)