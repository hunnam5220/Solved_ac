from sys import stdin

n = int(stdin.readline().rstrip())
result = 0

for step in range(1, n + 1):
    if step < 11:
        result += 1
    else:
        if step % sum(list(map(int, list(str(step))))) == 0:
            result += 1

print(result)