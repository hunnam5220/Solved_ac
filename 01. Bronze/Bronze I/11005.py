from sys import stdin

a, b = map(int, stdin.readline().split())
string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = ''

while a != 0:
    ans += str(string[a % b])
    a //= b

print(ans[::-1])