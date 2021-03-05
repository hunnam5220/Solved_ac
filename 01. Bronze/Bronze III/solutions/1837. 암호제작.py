from sys import stdin

p, k = map(int, stdin.readline().rstrip().split())


# 에라토스테네스의 체
def get_prime_arr(num):
    arr = [True] * num
    mm = int(num ** 0.5)

    for x in range(2, mm + 1):
        if arr[x]:
            for y in range(x + x, num, x):
                arr[y] = False

    return [i for i in range(2, num) if arr[i] == True]


p_ar = get_prime_arr(k)
x, y = 0, 0

for step in p_ar:
    if p % step == 0:
        x = step
        y = p // step
        break

if x == y == 0:
    print('GOOD')

else:
    print('BAD {}'.format(min([x, y])))
