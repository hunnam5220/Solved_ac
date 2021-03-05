from sys import stdin

n = int(stdin.readline().rstrip())
result = 0

for num in range(3, n+1):
    chk = num
    while 1:
        if chk < 3:
            break
        if chk % 10 == 3 or chk % 10 == 6 or chk % 10 == 9:
            result += 1
        chk //= 10

print(result)