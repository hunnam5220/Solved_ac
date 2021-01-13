from sys import stdin

bessie = list(map(int, stdin.readline().split()))
daisy = list(map(int, stdin.readline().split()))
goal = list(map(int, stdin.readline().split()))

cnt_b = 0
cnt_d = 0

while True:
    if bessie == goal:
        break

    elif (bessie[0] < goal[0]) and (bessie[1] < goal[1]):
        bessie[0] += 1
        bessie[1] += 1
        cnt_b += 1

    elif (bessie[0] > goal[0]) and (bessie[1] > goal[1]):
        bessie[0] -= 1
        bessie[1] -= 1
        cnt_b += 1

    elif (bessie[0] < goal[0]) and (bessie[1] > goal[1]):
        bessie[0] += 1
        bessie[1] -= 1
        cnt_b += 1

    elif (bessie[0] > goal[0]) and (bessie[1] < goal[1]):
        bessie[0] -= 1
        bessie[1] += 1
        cnt_b += 1

    elif bessie[0] < goal[0]:
        bessie[0] += 1
        cnt_b += 1

    elif bessie[0] > goal[0]:
        bessie[0] -= 1
        cnt_b += 1

    elif bessie[1] < goal[1]:
        bessie[1] += 1
        cnt_b += 1

    elif bessie[1] > goal[1]:
        bessie[1] -= 1
        cnt_b += 1

while True:
    if daisy == goal:
        break

    elif daisy[0] < goal[0]:
        daisy[0] += 1
        cnt_d += 1

    elif daisy[0] > goal[0]:
        daisy[0] -= 1
        cnt_d += 1

    elif daisy[1] < goal[1]:
        daisy[1] += 1
        cnt_d += 1

    elif daisy[1] > goal[1]:
        daisy[1] -= 1
        cnt_d += 1

if cnt_b < cnt_d:
    print('bessie')
elif cnt_b == cnt_d:
    print('tie')
else: print('daisy')
