from sys import stdin

arr = list(map(int, stdin.readline().split()))
msg = 'Soongsil Korea Hanyang'.split(' ')[arr.index(min(arr))]

if sum(arr) >= 100:
    print('OK')
else:
    print(msg)