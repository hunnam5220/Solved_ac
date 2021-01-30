from sys import stdin

a = list(map(int, stdin.readline().rstrip().split()))
b = list(map(int, stdin.readline().rstrip().split()))
w_a, w_b = 0, 0
winner = ''

for x, y in zip(a, b):
    if x < y:
        w_b += 3
        winner = 'B'

    elif x > y:
        w_a += 3
        winner = 'A'

    else:
        w_a += 1
        w_b += 1

print(w_a, w_b)

if w_a > w_b:
    print('A')

elif w_a < w_b:
    print('B')

elif winner != '' and w_a == w_b:
    print(winner)

else:
    print('D')