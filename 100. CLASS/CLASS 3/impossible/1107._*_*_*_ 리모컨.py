from sys import stdin

n = stdin.readline().rstrip()
m = int(stdin.readline())
d = set(stdin.readline().split())
button = set(str(x) for x in range(10))
if m > 0:
    button -= d

now_chan = 100
res = abs(now_chan - int(n))

for channel in range(1000000):
    for j in range(len(str(channel))):
        if str(channel)[j] not in button:
            break
        elif len(str(channel)) - 1 == j:
            res = min(res, abs(channel - int(n)) + len(str(channel)))

print(res)
