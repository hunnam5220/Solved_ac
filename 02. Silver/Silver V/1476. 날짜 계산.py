from sys import stdin

data = list(map(int, stdin.readline().split()))
ans = [1, 1, 1]
years = 1

while data != ans:
    ans[0] = ans[0] + 1 if ans[0] + 1 < 16 else 1
    ans[1] = ans[1] + 1 if ans[1] + 1 < 29 else 1
    ans[2] = ans[2] + 1 if ans[2] + 1 < 20 else 1
    years += 1


print(years)