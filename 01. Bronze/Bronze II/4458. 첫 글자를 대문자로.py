from sys import stdin

for i in range(int(stdin.readline())):
    data = list(stdin.readline().rstrip())
    data[0] = data[0].upper()

    print(''.join(data))