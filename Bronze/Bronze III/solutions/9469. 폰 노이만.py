from sys import stdin

# 기차가 만날 때까지만 파리는 날면 된다

for step in range(int(stdin.readline().rstrip())):
    n, d, a, b, f = list(stdin.readline().rstrip().split())
    n, d, a, b, f = int(n), float(d), float(a), float(b), float(f)
    time = d / (a + b)
    result = time * f

    print('%d %f' % (n, result))