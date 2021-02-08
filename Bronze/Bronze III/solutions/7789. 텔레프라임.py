from sys import stdin


def check_prime_num(num):
    n = int(num ** 0.5)
    for x in range(2, n+1):
        if num % x == 0:
            return False
    return True


num, p = map(int, stdin.readline().rstrip().split())

if check_prime_num(num) and check_prime_num(int(str(p) + str(num))):
    print('Yes')
else:
    print('No')

