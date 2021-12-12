from sys import stdin

n = int(stdin.readline())
nums = {x: 1 for x in range(10)}
arr = list(stdin.readline().split())
value = [-int(1e10), int(1e10)]


def check(s):
    idx = 0
    pre = s[0]
    for i in range(1, n + 1):
        if arr[idx] == '<':
            if pre < s[i]:
                idx += 1
                pre = s[i]
            else:
                return False

        elif arr[idx] == '>':
            if pre > s[i]:
                idx += 1
                pre = s[i]
            else:
                return False

    return True


def solve(cnt, s):
    if cnt > len(arr) + 1:
        return

    if cnt == len(arr) + 1:
        if check(s):
            if int(value[1]) > int(s):
                value[1] = s

            if int(value[0]) < int(s):
                value[0] = s
        return

    for i in nums:
        if nums[i] == 1:
            nums[i] -= 1
            solve(cnt + 1, s + str(i))
            nums[i] += 1


solve(0, '')
print(*value, sep='\n')