from sys import stdin
result = 0
for step in range(int(stdin.readline().rstrip())):
    if int(stdin.readline().rstrip()):
        result += 1
    else:
        result -= 1
if result > 0:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")