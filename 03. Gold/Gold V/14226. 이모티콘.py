from sys import stdin
import heapq


def solve(n):
    q = []
    heapq.heappush(q, (0, 1, 0))
    visited = set()

    while q:
        time, emoji, clipboard = heapq.heappop(q)

        if emoji == n:
            return time
        
        if (time + 1, emoji, emoji) not in visited:
            heapq.heappush(q, (time + 1, emoji, emoji))
            visited.add((time + 1, emoji, emoji))

        if (time + 1, emoji + clipboard, clipboard) not in visited:
            heapq.heappush(q, (time + 1, emoji + clipboard, clipboard))
            visited.add((time + 1, emoji + clipboard, clipboard))

        if (time + 1, emoji - 1, clipboard) not in visited:
            heapq.heappush(q, (time + 1, emoji - 1, clipboard))
            visited.add((time + 1, emoji - 1, clipboard))


print(solve(int(stdin.readline())))
