from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    n = int(stdin.readline().rstrip())
    cnt, grade = 0, 0
    for step2 in range(n):
        c, g = map(float, stdin.readline().rstrip().split())
        cnt += c
        grade += g * c

    print('%d %.1f' % (cnt, (grade / cnt)))