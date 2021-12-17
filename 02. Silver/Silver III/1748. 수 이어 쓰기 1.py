from sys import stdin

"""
ex) 12345
총 다섯자리 이며 1만 자리까지 있다.

1의 자리를 표현하는 방법은 1~9 => 한자리씩 아홉개 1 * 9
10의 자리를 표현하는 방법은 10~99 => 두자리씩 (99 + 1) - 10, 2 * 90개
100의 자리를 표현하는 방법은 100~999 => 세자리씩 3 * 900
1000의 자리를 표현하는 방법은 1000~9999 = > 네자리씩 4 * 9000

여기까지 ans에 저장하면 38889개
마지막은 10000~12345 = > 다섯자리씩 5 * 2346
이것을 ans 에 더해주면 결과값이 나온다.
"""


n = int(stdin.readline())
l = len(str(n))
ans = 0
k = 9
for i in range(l - 1):
    ans += k * (10 ** i) * (i + 1)

ans += ((n + 1) - 10 ** (l - 1)) * l
print(ans)