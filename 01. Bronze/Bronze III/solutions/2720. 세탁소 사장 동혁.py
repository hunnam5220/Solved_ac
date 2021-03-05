from sys import stdin

arr = [25, 10, 5, 1]

for step in range(int(stdin.readline().rstrip())):
    result = []
    cents = int(stdin.readline().rstrip())

    for c in arr:
        print(int(cents // c), end=' ')
        cents = cents % c

    print()