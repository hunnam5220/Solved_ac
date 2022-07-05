from sys import stdin

for i in range(1, int(stdin.readline()) + 1):
    print('String #{}'.format(i))
    string = stdin.readline().rstrip()
    answer = ''
    for j in string:
        temp = ord(j) + 1 if ord(j) + 1 < 91 else 65
        answer += chr(temp)
    print(answer, '\n')