from sys import stdin
import sys
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
l, r = 0, n - 1
ans_l = 0
ans_r = 0
min_val = sys.maxsize


while l < r:
    # 현재 포인터로 잡혀있는 두개의 값을 더해준다.
    sum_val = arr[l] + arr[r]

    # 두 포인터가 가리키는 값의 합이 가장 작은 값보다 작으면
    if abs(sum_val) < min_val:

        # 두 포인터를 정답으로 할 변수에 저장한다.
        ans_l = l
        ans_r = r

        # 최솟값 갱신
        min_val = abs(sum_val)

    # 두 수의 합이 0보다 크면 오른쪽 포인터를 1 줄인다.
    if sum_val > 0:
        r -= 1

    # 두 수의 0보다 작으면 왼쪽 포인터를 1 키운다
    elif sum_val < 0:
        l += 1
    else:
        break

print(arr[ans_l], arr[ans_r])
