from sys import stdin

n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().rstrip().split()))
result = 0
case = 0

for s in arr:
    if case == s:
        result += 1
        case += 1
        if case == 3:
            case = 0


print(result)