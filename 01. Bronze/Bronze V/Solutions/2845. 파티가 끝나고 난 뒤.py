from sys import stdin

ipt = stdin.readline

l, p = ipt().rstrip().split()
num_of_human = int(l) * int(p)

article_human = list(map(int, ipt().rstrip().split()))

for human in article_human:
    print(human - num_of_human, end=' ')