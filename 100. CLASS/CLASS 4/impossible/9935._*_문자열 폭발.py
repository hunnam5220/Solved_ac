from sys import stdin

string = stdin.readline().rstrip()
bomb = stdin.readline().rstrip()
b_len = len(bomb)
stack = []
for s in string:
    stack.append(s)
    if stack[-1] == bomb[-1]:
        if stack[-b_len:] == list(bomb):
            for _ in range(b_len):
                stack.pop()

if stack:
    print(*stack, sep='')
else:
    print("FRULA")