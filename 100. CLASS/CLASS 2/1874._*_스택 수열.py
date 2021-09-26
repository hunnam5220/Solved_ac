from sys import stdin

res, stack = [], []
cnt, x = 0, 1

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())

    while cnt < n:
        cnt += 1
        stack.append(cnt)
        res.append("+")

    top = stack[-1]
    if stack[-1] == n:
        stack.pop()
        res.append("-")
    else:
        x = 0
        break

if not x:
    print("NO")
else:
    for i in res:
        print(i)