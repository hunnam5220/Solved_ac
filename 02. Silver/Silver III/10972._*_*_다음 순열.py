from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))


for i in range(n-1, -1, -1):
    if i == 0:
        print(-1)
        break

    if arr[i - 1] < arr[i]:
        fi, si = i-1, i

        for j in range(n - 1, fi, -1):
            if arr[j] > arr[fi]:
                temp = arr[j]
                arr[j], arr[fi] = arr[fi], temp

                temp1 = arr[:si]
                temp2 = arr[si:]
                temp2.sort()
                temp1 += temp2
                print(*temp1)
                exit()