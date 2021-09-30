from sys import stdin

arr = [0 for _ in range(501)]
pre = 1
for i in range(5, 501):
    if i % 5 == 0:
        res = 0
        tmp = i
        while 1:
            res += tmp // 5
            tmp //= 5
            if tmp == 0:
                pre = res
                arr[i] = res
                break
    else:
        arr[i] = pre

print(arr[int(stdin.readline())])