from sys import stdin

k = [1, 2, 3, 4, 5, 6, 7, 8]
arr = list(map(int, stdin.readline().split()))
d = sorted(k, reverse=True)

if arr == k:
    print("ascending")
elif arr == d:
    print("descending")
else:
    print("mixed")
