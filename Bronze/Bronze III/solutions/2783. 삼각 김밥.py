from sys import stdin

price = []
seven25 = list(map(int, stdin.readline().rstrip().split()))
price.append(seven25[0] * (1000 / seven25[1]))

n = int(stdin.readline().rstrip())

another = []
for step in range(n):
    another.append(list(map(int, stdin.readline().rstrip().split())))

for step in range(n):
    price.append(another[step][0] * (1000 / another[step][1]))

print(min(price))
