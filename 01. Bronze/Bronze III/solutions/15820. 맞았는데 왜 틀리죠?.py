from sys import stdin

s1, s2 = map(int, stdin.readline().rstrip().split())
msg = 'Accepted'

for step in range(s1):
    a, b = map(int, stdin.readline().split())

    if a != b:
        msg = 'Wrong Answer'

for step in range(s2):
    a, b = map(int, stdin.readline().split())

    if a != b and msg != 'Wrong Answer':
        msg = 'Why Wrong!!!'

print(msg)