from sys import stdin

n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().rstrip().split()))

y_p = 0
m_p = 0

for step in range(n):
    y_p += 10 * (arr[step] // 30 + 1)
    m_p += 15 * (arr[step] // 60 + 1)

if y_p == m_p:
    print('Y', end=' ')
    print('M', end=' ')
    print(y_p, end=' ')

elif y_p < m_p:
    print('Y', end=' ')
    print(y_p, end=' ')
else:
    print('M', end=' ')
    print(m_p, end=' ')