from sys import stdin

n = int(stdin.readline())
arr = [str(x) for x in range(666, int(2666850))]
res = set()
cnt = 0
for i in arr:
    if '666' in i:
        res.add(int(i))
        cnt += 1
        if cnt == n:
            break

res = list(res)
res.sort()
print(res[n - 1])