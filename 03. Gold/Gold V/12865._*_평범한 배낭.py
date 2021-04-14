from sys import stdin

# 물품의 수, 제한 무게
n, k = map(int, stdin.readline().split())

bag = []
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    bag.append((a, b))

# k + 1 크기의 knap 생성
knap = [0 for _ in range(k + 1)]


for i in range(n):
    for j in range(k, 1, -1):
        if bag[i][0] <= j:
            knap[j] = max(knap[j], knap[j - bag[i][0]] + bag[i][1])

print(max(knap))

"""
4 7
6 13
4 8
3 6
5 12

4 1
6 13
4 8
3 6
5 12

8 4
1 3
1 6
1 3
1 3
1 3
1 2
1 5
1 8
"""
