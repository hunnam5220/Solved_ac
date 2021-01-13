from sys import stdin
st = stdin.readline().rstrip().replace('=', '==')

if eval(st):
    print('YES')
else:
    print('NO')