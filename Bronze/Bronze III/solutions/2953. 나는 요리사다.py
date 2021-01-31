from sys import stdin

arr = []
for x in range(5):
    arr.append(sum(list(map(int, stdin.readline().rstrip().split()))))
m = max(arr)
print(arr.index(m)+1, m)