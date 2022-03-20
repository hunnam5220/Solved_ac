from sys import stdin

score = list(map(int, stdin.readline().split()))
my_score = int(stdin.readline())
grade = 1

for i in range(50):
    if score[i] > my_score:
        grade += 1
    else:
        break

if 1 <= grade <= 5:
    print('A+')
elif 5 < grade <= 15:
    print('A0')
elif 15 < grade <= 30:
    print('B+')
elif 30 < grade <= 35:
    print('B0')
elif 35 < grade <= 45:
    print('C+')
elif 45 < grade <= 48:
    print('C0')
else:
    print('F')
