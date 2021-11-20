from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

arr = []
for _ in range(9):
    arr.append(list(map(int, list(stdin.readline().rstrip()))))

# 행 숫자 검사용
c1 = [[False] * 10 for _ in range(9)]

# 열 숫자 검사용
c2 = [[False] * 10 for _ in range(9)]

# 사각형 숫자 검사용
c3 = [[False] * 10 for _ in range(9)]


def calc(x, y):
    return (x // 3) * 3 + (y // 3)


def solve(n):
    # 칸 81개 다 채웠으면 출력
    if n == 81:
        for i in arr:
            print(''.join(map(str, i)))
        return True

    # 좌표 구하기
    x = n // 9
    y = n % 9

    # 채우지 않아도 된다면 재귀호출
    if arr[x][y]:
        return solve(n + 1)

    else:
        # 답이 여러개면 적은 숫자를 출력해야한다.
        # 그러니까 1부터 10까지 순회하면서 행, 열,
        # 3*3 배열에 모두 쓰이지 않은 숫자 중 가장 작은 것부터 집어넣는다.
        for i in range(1, 10):
            if not c1[x][i] and not c2[y][i] and not c3[calc(x, y)][i]:
                c1[x][i] = c2[y][i] = c3[calc(x, y)][i] = True
                arr[x][y] = i
                if solve(n + 1):
                    return True
                c1[x][i] = c2[y][i] = c3[calc(x, y)][i] = False
                arr[x][y] = 0

    return False


# 이미 채워져 있는 숫자를 False 에서 True 로 변경
for i in range(9):
    for j in range(9):
        if arr[i][j]:
            c1[i][arr[i][j]] = True
            c2[j][arr[i][j]] = True
            c3[calc(i, j)][arr[i][j]] = True

solve(0)