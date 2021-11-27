from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


def solve(start, end):
    if start > end:
        return

    div = end + 1
    for i in range(start + 1, end + 1):
        if nodes[start] < nodes[i]:
            div = i
            break

    solve(start + 1, div - 1)
    solve(div, end)
    print(nodes[start])


nodes = []

while 1:
    node = stdin.readline().rstrip()
    if not node:
        break
    else:
        nodes.append(int(node))

solve(0, len(nodes) - 1)