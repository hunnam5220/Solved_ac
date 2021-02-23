t = sum(list(map(int, input().split())))
c = int(input())
if t < c * 2:
    print(t)
else:
    print(t - c * 2)