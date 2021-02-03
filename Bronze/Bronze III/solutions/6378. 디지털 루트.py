from sys import stdin

while 1:
    n = stdin.readline().rstrip()

    if len(n) == 1 and int(n[0]) == 0:
        break

    arr = list(n)

    while 1:
        if len(str(eval('+'.join(arr)))) == 1:
            result = eval('+'.join(arr))
            break

        else:
            arr = list(str(eval('+'.join(arr))))

    print(result)