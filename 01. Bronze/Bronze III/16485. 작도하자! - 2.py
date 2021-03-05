from sys import stdin

# 삼각형 ABC, 각 BAC의 이등분선과 변 BC의 교점 B
# AB의 길이 c, AC의 길이 b가 주어질 때,
# 선분 bm / 선분 cm 의 값은 c / b와 같다.
c, b = map(int, stdin.readline().rstrip().split())
print('%.7f' % (c / b))