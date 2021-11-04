from sys import stdin

""" # 좌표를 가진 다각형의 면적구하기 
n = 4
a = [0, 0]
b = [0, 10]
c = [10, 10]
d = [10, 0]

일 때, 
((a[0] * b[1] + b[0] * c[1] + c[0] * d[1] + d[0] * a[1]) - (a[1] * b[0] + b[1] * c[0] + c[1] * d[0] + d[1] * a[0])) / 2

를 해주면 면적이 나온다.
"""

edges = []
step = int(stdin.readline())
for i in range(step):
    edges.append(list(map(int, stdin.readline().split())))
edges.append(edges[0])

a, b = 0, 0
for i in range(step):
    a += edges[i][0] * edges[i + 1][1]
    b += edges[i][1] * edges[i + 1][0]

if b > a:
    print(round((a + b) / 2, 1))
else:
    print(round((a - b) / 2, 1))