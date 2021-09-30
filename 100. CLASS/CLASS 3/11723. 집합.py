from sys import stdin

res = set()
all = set([x for x in range(1, 21)])
for _ in range(int(stdin.readline())):
    command = stdin.readline().split()
    if len(command) == 2:
        a, b = command
        b = int(b)
        if a == 'add':
            res.add(b)

        elif a == 'check':
            print(0) if len({b} - res) else print(1)

        elif a == 'remove':
            res -= {b}

        elif a == 'toggle':
            if len(res - {b}) != len(res):
                res -= {b}
            else:
                res.add(b)

    elif command[0] == 'all':
        res = all

    elif command[0] == 'empty':
        res.clear()