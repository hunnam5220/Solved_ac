from collections import deque
from sys import stdin

n = int(stdin.readline())
nums = [int(stdin.readline()) for _ in range(n)]
checker = list(sorted(nums))
queues = deque()
queues.append(deque())
queues[0].append(nums[0])

for i in range(1, n):
    num = nums[i]
    tf = False

    for j in range(len(queues)):
        if queues[j][0] > num:
            if abs(checker.index(queues[j][0]) - checker.index(num)) == 1:
                queues[j].appendleft(num)
                tf = True
                break

        elif queues[j][-1] < num:
            if abs(checker.index(queues[j][-1]) - checker.index(num)) == 1:
                queues[j].append(num)
                tf = True
                break

    if not tf:
        temp = deque()
        temp.append(num)
        queues.append(temp)


print(len(queues))