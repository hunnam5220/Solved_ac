from sys import stdin

n = int(stdin.readline().rstrip())
'''
# 여분 > 3 세개를 제외한 3의 개수
n       여분
9       0
12      1
15      2
18      3
21      4
...
3000    97

여분 개수가 증가 됨에 따라 증가되는 경우의 수 p가 1씩 증가되어 누적된다.
'''
result = 1
p = 2
if n > 8:
    k = n // 3 - 3

    for step in range(k):
        result += p
        p += 1

    print(result)
else:
    print(0)