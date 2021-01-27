from sys import stdin


# 에라토스테네스의 체
def get_prime_arr(num):
    arr = [True] * num
    mm = int(num ** 0.5)

    for x in range(2, mm + 1):
        if arr[x]:
            for y in range(x + x, num, x):
                arr[y] = False

    return [i for i in range(2, num) if arr[i] is True]


k, l = map(int, stdin.readline().rstrip().split())

p_arr = get_prime_arr(k)
print(p_arr)
