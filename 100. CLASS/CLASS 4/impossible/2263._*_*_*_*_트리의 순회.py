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
"""

10
1 3 2 5 4 6 8 7 10 9
1 2 3 4 5 8 10 9 7 6
답: 6 5 3 1 2 4 7 8 9 10 

 

21

1 3 2 7 4 6 5 15 11 9 12 8 13 10 14 21 19 17 20 16 18

1 2 3 4 5 6 7 11 12 9 13 14 10 8 15 19 20 17 18 16 21

답: 21 15 7 3 1 2 6 4 5 8 9 11 12 10 13 14 16 17 19 20 18

"""
