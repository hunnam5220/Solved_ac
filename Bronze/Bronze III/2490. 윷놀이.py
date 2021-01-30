from sys import stdin
from collections import Counter as cc

result_dict = {
    1: 'A',
    2: 'B',
    3: 'C',
}

for step in range(3):
    arr = list(map(int, stdin.readline().rstrip().split()))

    chk = sorted(cc(arr).items(), key=lambda x: x[0])[0][1]

    if 0 < chk < 4:
        print(result_dict[chk])
    else:
        if arr[0] == 1:
            print('E')
        else:
            print('D')