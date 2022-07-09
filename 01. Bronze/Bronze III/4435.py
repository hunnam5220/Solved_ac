from sys import stdin

gan = [1, 2, 3, 3, 4, 10]
sa = [1, 2, 2, 2, 3, 5, 10]

for b in range(int(stdin.readline())):
    answer = 'Battle {}: '.format(b + 1)
    temp1, temp2 = 0, 0
    g, s = list(map(int, stdin.readline().split())), list(map(int, stdin.readline().split()))
    for i in range(len(g)):
        temp1 += g[i] * gan[i]

    for i in range(len(s)):
        temp2 += s[i] * sa[i]

    if temp1 > temp2:
        answer += 'Good triumphs over Evil'
    elif temp1 < temp2:
        answer += 'Evil eradicates all trace of Good'
    else:
        answer += 'No victor on this battle field'

    print(answer)