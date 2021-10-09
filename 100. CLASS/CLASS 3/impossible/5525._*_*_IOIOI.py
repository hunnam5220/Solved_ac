from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
s = stdin.readline().rstrip()
pattern, res = 0, 0

for i in range(1, m - 1):
    if s[i-1] == 'I' and s[i] == 'O' and s[i + 1] == 'I':
        pattern += 1
        if pattern == n:
            res += 1
            pattern -= 1
    elif s[i-1] == 'O' and s[i] == 'I' and s[i + 1] == 'O':
        pass

    else:
        pattern = 0

print(res)