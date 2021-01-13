from sys import stdin

arr = list(map(int, stdin.readline().split()))
h = max(arr)
w = min(arr)

if h > w * 3:
    print(w)

elif h > w * 1.5:
    print(h / 3)

else:
    print(w / 2)