from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

n = int(stdin.readline())
inorder = list(map(int, stdin.readline().split()))
postorder = list(map(int, stdin.readline().split()))


def solve(in_s, in_e, post_s, post_e):
    if (in_s > in_e) or (post_s > post_e):
        return

    parents = postorder[post_e]
    print(parents, end=" ")

    left = pos[parents] - in_s
    right = in_e - pos[parents]

    solve(in_s, in_s + left - 1, post_s, post_s + left - 1)
    solve(in_e - right + 1, in_e, post_e - right, post_e - 1)


pos = [0 for _ in range(n + 1)]
for i in range(n):
    pos[inorder[i]] = i

solve(0, n - 1, 0, n - 1)