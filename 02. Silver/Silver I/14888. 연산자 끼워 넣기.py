from sys import stdin
from itertools import permutations
from collections import deque

n = int(stdin.readline().rstrip())
arr = list(stdin.readline().rstrip().split())
cal = []
d = {0: '+', 1: '-', 2: '*', 3: '/'}


def get_calc_val(cal_st):
    nq = deque(arr)
    dq = deque(list(cal_st))
    val, u, s = None, None, None

    while 1:
        if nq:
            if val is not None:
                u = int(nq.popleft())
                if s == '+':
                    val += u
                elif s == '-':
                    val -= u
                elif s == '*':
                    val *= u
                elif s == '/':
                    if val < 0 and u > 0:
                        val = abs(val) // u * -1
                    elif u == 0:
                        val = 0
                    else:
                        val //= u

                u, s = None, None
            else:
                val = int(nq.popleft())

        if dq and s is None:
            s = dq.popleft()

        if not dq and not nq:
            break

    return val


for x, i in zip(list(map(int, stdin.readline().split())), range(4)):
    for _ in range(x):
        cal.append(d[i])

cal_prod = list(set(permutations(cal, len(cal))))

max_val = int(1e9) * -1
min_val = int(1e9)

for step in range(len(cal_prod)):
    val = get_calc_val(cal_prod[step])

    if val < min_val:
        min_val = val

    if val > max_val:
        max_val = val

print(max_val)
print(min_val)