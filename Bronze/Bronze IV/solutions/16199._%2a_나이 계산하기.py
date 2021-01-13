y, m, d = map(int, input().split())
a, b, c = map(int, input().split())
print(a - y - (0 if m < b or (m == b and d <= c) else 1), a - y + 1, a - y, sep='\n')
