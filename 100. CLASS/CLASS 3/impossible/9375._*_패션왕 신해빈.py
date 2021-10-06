from sys import stdin


for _ in range(int(stdin.readline())):
    cloth = {}
    n = int(stdin.readline())
    if n == 0:
        print(0)
    else:
        for __ in range(n):
            data = list(stdin.readline().rstrip().split())

            if data[1] not in cloth:
                cloth[data[1]] = 1
            else:
                cloth[data[1]] += 1

        if len(cloth) == 1:
            print(list(cloth.values())[0])
        else:
            temp = 1
            for i in cloth.values():
                temp *= (i + 1)
            temp -= 1
            print(temp)