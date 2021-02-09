from sys import stdin

while 1:
    try:
        n, p = map(int, stdin.readline().rstrip().split())
        x_arr = [x for x in range(1, n+1)]
        y_arr = list(reversed(x_arr))

        pages = []

        for step in range(n // 4):
            pages.append([y_arr.pop(), y_arr.pop(), x_arr.pop(), x_arr.pop()])

        for step in pages:
            try:
                t = step.index(p)

                del step[t]
                for q in sorted(step):
                    print(q, end=' ')
                print()
                break
            except:
                continue

    except:
        break