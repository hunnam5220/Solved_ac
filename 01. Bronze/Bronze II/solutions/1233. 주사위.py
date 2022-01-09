from sys import stdin

a, b, c = map(int, stdin.readline().split())
d = {}

for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            temp = i + j + k
            if temp not in d:
                d[temp] = 1
            else:
                d[temp] += 1


ans = [-1, -1]
for key, item in d.items():
    if ans[1] < item:
        ans = [key, item]

print(ans[0])