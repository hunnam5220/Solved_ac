from sys import stdin
import heapq

q = []


for i in range(int(stdin.readline())):
    x = int(stdin.readline())
    if x == 0:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q) * -1)

    heapq.heappush(q, -x)