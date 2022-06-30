from sys import stdin

data = stdin.readline().rstrip()
a, b = 0, 0
for i in range(0, len(data), 2):
    team, score = data[i: i + 2]
    score = int(score)
    if team == 'A':
        a += score
    elif team == 'B':
        b += score

    if a == b == 10:
        a -= 2
        b -= 2
        continue

    if a >= 11:
        print('A')
        exit()

    elif b >= 11:
        print('B')
        exit()


if a < b:
    print('B')

elif a > b:
    print('A')