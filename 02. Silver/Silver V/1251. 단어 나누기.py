from sys import stdin
from copy import deepcopy

string = list(stdin.readline().rstrip())
length = len(string)
ans = []


# 세 단어 뒤집고 합치기
def get_string(array):
    temp = deepcopy(array)
    res = ''
    for i in temp:
        i.reverse()
        res += ''.join(i)

    ans.append(res)


def solve(cnt, arr, last_idx):
    global length

    if cnt == 2:
        arr.append(string[last_idx - 1:])
        get_string(arr)
        arr.pop()
        return

    for i in range(last_idx, length):
        arr.append(string[last_idx - 1:i])
        solve(cnt + 1, arr, i + 1)
        arr.pop()


solve(0, [], 1)
ans.sort()
print(ans[0])
