from sys import stdin

n = int(stdin.readline())
string = stdin.readline().rstrip()
d = {}
for i in range(n):
    d[chr(i + 65)] = int(stdin.readline())

stack = []
for i in string:
    if i.isalpha():
        stack.append(d[i])
    else:
        a = stack.pop()
        b = stack.pop()
        if i == '+':
            stack.append(b + a)

        elif i == '-':
            stack.append(b - a)

        elif i == '*':
            stack.append(b * a)

        else:
            stack.append(b / a)

print('%.2f' % stack[0])