from sys import stdin
import heapq
q = []
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, n)
