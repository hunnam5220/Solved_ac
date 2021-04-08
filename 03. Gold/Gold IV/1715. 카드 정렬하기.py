from sys import stdin
import heapq

arr = []
for r in range(int(stdin.readline().rstrip())):
    heapq.heappush(arr, int(stdin.readline().rstrip()))

result = 0
while len(arr) != 1:
    _1 = heapq.heappop(arr)
    _2 = heapq.heappop(arr)

    sum_val = _1 + _2
    result += sum_val
    heapq.heappush(arr, sum_val)

print(result)
