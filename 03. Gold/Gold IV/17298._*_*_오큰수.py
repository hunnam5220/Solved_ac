from sys import stdin

n = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
answer = [-1] * n
stack = [0]

for i in range(n):
    while stack and data[stack[-1]] < data[i]:
        answer[stack.pop()] = data[i]
    stack.append(i)

print(*answer)