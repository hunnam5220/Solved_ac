from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

# 방문 횟수를 더해서 저장할 변수
result = 0


def solve(n, x, y):
    global result

    # x, y 가 구하려고 하는 지점에 도달한 경우 결과를 출력하고 None 반환
    if x == r and y == c:
        print(result)
        return

    # n 이 1일 경우 2 * 2 블럭이다.
    # 분할정복의 알고리즘에 의해 한칸씩 탐색하며, 결과값에 +1 을 해준다.
    if n == 1:
        result += 1
        return

    # 현재 분할되어 내가 탐색하고 있는 좌표 구간의 범위 안에
    # 내가 구하려는 좌표가 있지 않으면 방문횟수를 result 에 더해준다.
    if not (x <= r < x + n and y <= c < y + n):
        result += n * n
        return

    # n * n 크기의 배열이기에 n을 2로 나눈 몫을 넣고, 탐색을 시작한다.
    # 1사분면 탐색
    solve(n // 2, x, y)

    # 2사분면 탐색
    solve(n // 2, x, y + n // 2)

    # 3사분면 탐색
    solve(n // 2, x + n // 2, y)

    # 4사분면 탐색
    solve(n // 2, x + n // 2, y + n // 2)


n, r, c = map(int, stdin.readline().split())
# (0, 0) 부터 시작해서 방문 횟수를 더해준다.
solve(2 ** n, 0, 0)