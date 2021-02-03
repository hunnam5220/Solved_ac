from sys import stdin


# 유클리드 호제법
def gcd(m, n):
    while n != 0:
        t = m % n
        (m, n) = (n, t)
    return abs(m)


# 두 개 이상의 수의 공약수는 두 수의 최대공약수의 약수들
k = int(stdin.readline().rstrip())
arr = sorted(list(map(int, stdin.readline().rstrip().split())))

# 최대공약수 구하기
g = gcd(arr[0], arr[1])

if arr[-1] % g != 0:
    g = gcd(arr[-1], g)

result = []
step = 1

# 최대공약수의 약수를 출력
for step in range(1, g+1):
    if g % step == 0:
        if step not in result:
            result.append(step)

        if (g // step) not in result:
            result.append((g // step))

        else:
            break


for step in sorted(result):
    print(step)