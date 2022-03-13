from sys import stdin

arr = []
for _ in range(4):
    arr.append(int(stdin.readline()))

if arr[0] in [8, 9] and arr[1] == arr[2] and arr[3] in [8, 9]:
    print('ignore')
else:
    print('answer')