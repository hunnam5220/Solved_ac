from sys import stdin


def matrix_mul_self(n):
    base = [[1, 1], [1, 0]]
    result = [[1, 1], [1, 0]]

    for _ in range(n):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += (base[i][k] * base[k][j]) % 1000000007
        base = result
    return base


def matrix_mul(a, b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += (a[i][k] * b[k][j]) % 1000000007
    return result


n = bin(int(stdin.readline()))[2:]

result = [[1, 0], [0, 1]]
for i in range(len(n)):
    if n[-1-i] == '1':
        result = matrix_mul(result, matrix_mul_self(i))

print(result[0][1] % 1000000007)