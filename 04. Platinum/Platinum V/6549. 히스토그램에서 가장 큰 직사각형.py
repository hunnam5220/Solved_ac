from sys import stdin

while 1:
    data = list(map(int, stdin.readline().split()))
    n = data.pop(0)
    if n == 0:
        break

    q = []
    ans = 0

    for i in range(n):
        while len(q) != 0 and data[q[-1]] > data[i]:
            temp = q.pop()

            if len(q) == 0:
                w = i

            else:
                w = i -  q[-1] - 1

            ans = max(ans, w * data[temp])
        q.append(i)

    while len(q) != 0:
        temp = q.pop()

        if len(q) == 0:
            w = n
        else:
            w = n - q[-1] - 1

        ans = max(ans, w * data[temp])

    print(ans)