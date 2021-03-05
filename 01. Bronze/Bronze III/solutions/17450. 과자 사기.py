from sys import stdin

arr = ['S', 'N', 'U']
k = -1
for step in range(3):
    a, b = map(int, stdin.readline().split())

    if a * 10 >= 5000:
        disc = 500
    else:
        disc = 0

    result = b * 10 / (a * 10 - disc)

    if result > k:
        k = result
        msg = arr[step]

print(msg)