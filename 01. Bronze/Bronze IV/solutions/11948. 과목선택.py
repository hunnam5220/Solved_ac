from sys import stdin

mhsj = []
yz = []

for x in range(6):
    if len(mhsj) == 4:
        yz.append(int(stdin.readline().rstrip()))
    else:
        mhsj.append(int(stdin.readline().rstrip()))

mhsj = sorted(mhsj, reverse=True)
yz = sorted(yz, reverse=True)

print(sum(mhsj[:3]) + yz[0])