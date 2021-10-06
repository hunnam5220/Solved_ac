from sys import stdin
import heapq

for _ in range(int(stdin.readline())):
    min_q, max_q, visited = [], [], [True] * 1_000_001

    for i in range(int(stdin.readline())):
        c, num = stdin.readline().rstrip().split()
        num = int(num)
        if c == 'I':
            heapq.heappush(min_q, (num, i))
            heapq.heappush(max_q, (num * -1, i))

        else:
            if num == 1:
                while max_q and not visited[max_q[0][1]]:
                    heapq.heappop(max_q)
                if max_q:
                    visited[max_q[0][1]] = False
                    heapq.heappop(max_q)
            else:
                while min_q and not visited[min_q[0][1]]:
                    heapq.heappop(min_q)
                if min_q:
                    visited[min_q[0][1]] = False
                    heapq.heappop(min_q)

    while min_q and not visited[min_q[0][1]]:
        heapq.heappop(min_q)

    while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)

    if min_q and max_q:
        print(max_q[0][0] * -1, min_q[0][0])
    else:
        print('EMPTY')