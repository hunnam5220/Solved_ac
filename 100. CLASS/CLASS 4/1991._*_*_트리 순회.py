from sys import stdin

n = int(stdin.readline())
treelist = []


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


for i in range(n):
    a, b, c = list(stdin.readline().rstrip().split())
    node = Node(a)
    if b == '.':
        b = ''

    if c == '.':
        c = ''

    node.left = b
    node.right = c
    treelist.append(node)


def preorder(node):
    print(node.data, end='')
    if node.left != '':
        preorder(node.left)
    if node.right != '':
        preorder(node.right)


def inorder(node):
    if node.left != '':
        inorder(node.left)

    print(node.data, end='')
    if node.right != '':
        inorder(node.right)


def postorder(node):
    if node.left != '':
        postorder(node.left)

    if node.right != '':
        postorder(node.right)
    print(node.data, end='')


for i in range(n):
    for j in range(n):
        if treelist[i].data == treelist[j].left:
            treelist[j].left = treelist[i]

        elif treelist[i].data == treelist[j].right:
            treelist[j].right = treelist[i]

preorder(treelist[0])
print()
inorder(treelist[0])
print()
postorder(treelist[0])
print()
