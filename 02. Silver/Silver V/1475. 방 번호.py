from sys import stdin

n = stdin.readline().rstrip()
card_cnt = 1
card_set = {x:1 for x in range(10)}

for i in n:
    if int(i) == 6 or int(i) == 9:
        if card_set[6]:
            card_set[6] -= 1
        elif card_set[9]:
            card_set[9] -= 1
        else:
            card_cnt += 1
            for j in range(10):
                card_set[j] += 1

            card_set[int(i)] -= 1

    elif card_set[int(i)]:
        card_set[int(i)] -= 1

    else:
        card_cnt += 1
        for j in range(10):
            card_set[j] += 1
        card_set[int(i)] -= 1

print(card_cnt)