from sys import stdin

time = 0

for x in range(4):
    time += int(stdin.readline().rstrip())

print(time // 60)
print(time % 60)