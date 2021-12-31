from sys import stdin
import heapq

left_queue = []
right_queue = []
answer = []
for i in range(int(stdin.readline())):
    data = int(stdin.readline())
    if len(left_queue) == len(right_queue):
        heapq.heappush(left_queue, (-data, data))

    else:
        heapq.heappush(right_queue, (data, data))

    if right_queue and left_queue[0][1] > right_queue[0][0]:
        min_value = heapq.heappop(right_queue)[0]
        max_value = heapq.heappop(left_queue)[1]
        heapq.heappush(left_queue, (-min_value, min_value))
        heapq.heappush(right_queue, (max_value, max_value))

    answer.append(left_queue[0][1])

for j in answer:
    print(j)