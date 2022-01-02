from sys import stdin


n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
cluster = int(stdin.readline())
res = 0

for data in arr:
    if data <= cluster and data != 0:
        res += cluster
    elif data > cluster:
        temp = data // cluster
        if data - temp * cluster > 0:
            res += ((temp + 1) * cluster)
        else:
            res += (temp * cluster)

print(res)