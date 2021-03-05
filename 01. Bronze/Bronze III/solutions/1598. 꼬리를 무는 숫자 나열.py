from sys import stdin

arr = sorted(list(map(int, stdin.readline().split())))
cnt = 0
a, b = arr[0], arr[1]

if a % 4 == b % 4:
    print((b - a) // 4)

elif (a % 4 > b % 4 and b % 4 != 0) or a % 4 == 0:
    l = (b - a) // 4 + 1
    r = a + (l * 4) - b
    print(r + (b - a) // 4 + 1)

else:
    l = (b - a) // 4
    r = abs(a + (l * 4) - b)
    print(r + (b - a) // 4)