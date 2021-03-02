from sys import stdin
price = {
    1: 500,
    2: 800,
    3: 1000,
}
k = 5000
for step in list(map(int, stdin.readline().rstrip().split())):
    k -= price[step]
print(k)