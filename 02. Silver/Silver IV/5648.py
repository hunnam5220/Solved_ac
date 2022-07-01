from sys import stdin

data = list(map(int, stdin.readline().split()))
answer = []

if len(data) == 1:
    n = data[0]

else:
    n = data[0]
    n -= (len(data) - 1)

    for i in range(1, len(data)):
        answer.append(int(str(data[i])[::-1]))

    while n != 0:
        data = list(map(int, stdin.readline().split()))
        for i in range(len(data)):
            answer.append(int(str(data[i])[::-1]))

        n -= len(data)

for i in sorted(answer):
    print(i)
