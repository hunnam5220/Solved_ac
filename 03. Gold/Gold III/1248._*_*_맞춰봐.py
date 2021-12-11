from sys import stdin


def ck(idx):
    hap = 0
    # result 값을 더해나가면 부호랑 같나요?
    for i in range(idx, -1, -1):
        hap += result[i]
        if hap == 0 and S[i][idx] != 0:
            return False
        elif hap < 0 and S[i][idx] >= 0:
            return False
        elif hap > 0 and S[i][idx] <= 0:
            return False
    return True


def solve(idx):

    if idx == N:
        return True

    if S[idx][idx] == 0:
        # 부호 없는 숫자, 0일경우 결과값을 반환할 resuLt 에 해당하는 배열값을 0으로 저장
        result[idx] = 0
        return solve(idx + 1)

    # 각 자리에 알맞은 부호에 맞춰 숫자를 저장한다.
    for i in range(1, 11):
        result[idx] = S[idx][idx] * i

        # 숫자가 맞는지 체크
        if ck(idx) and solve(idx + 1):
            return True

    return False


N = int(stdin.readline())
arr = list(stdin.readline().rstrip())

# i부터 n까지 해당하는 각 구간합에 대한 부호를 저장한다.
S = [[0] * N for i in range(N)]
for i in range(N):
    for j in range(i, N):
        temp = arr.pop(0)
        if temp == '+':
            S[i][j] = 1
        elif temp == '-':
            S[i][j] = -1

# 결과를 보여줄 리스트
result = [0] * N
solve(0)
print(*result)
