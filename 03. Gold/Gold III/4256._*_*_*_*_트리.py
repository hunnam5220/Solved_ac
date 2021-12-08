from sys import stdin


def solve(s, e):
    global idx

    if s == e:
        print(inorder[s], end=' ')
        idx += 1
        return

    elif s > e:
        return

    # root 찾은 시점부터 idx가 필요가 없다.
    root_index = inorder.index(preorder[idx])
    idx += 1

    solve(s, root_index - 1)

    # 다음에 찾아봐야할 idx 의 증가하는 식은
    # 이미 왼쪽 서브트리를 찾을 때 일어났기 때문에
    # 여기에서 idx + 1 을 해줄 필요가 없다.
    solve(root_index + 1, e)
    print(inorder[root_index], end=' ')


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    preorder = list(map(int, stdin.readline().split()))
    inorder = list(map(int, stdin.readline().split()))

    idx = 0
    solve(0, n - 1)
    print()