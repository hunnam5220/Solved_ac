from collections import deque
from sys import stdin


def solve(root):
    q = deque()
    # 시작 노드를 큐에 추가
    q.append(root)
    krr[root] = 1

    while q:
        now = q.popleft()

        # 시작노트로부터 방문이 가능한 노드들을 순회하며 방문
        for i in arr[now]:
            # 아직 그룹으로 묶이지 않은 노드라면
            if krr[i] == 0:
                q.append(i)
                # 시작한 노드로부터 연결된 정점을 -1을 곱해 데이터를 입력하고 연결해준다.
                krr[i] = -krr[now]
            else:
                # 만약 같은 그룹끼리 연결되어 있다면 False
                if krr[i] == krr[now]:
                    return False
    return True


# 테스트 케이스 개수만큼 반복
for _ in range(int(stdin.readline())):

    # 노드의 개수 v, 간선의 개수 e
    v, e = map(int, stdin.readline().split())

    # 노드의 개수만큼 이차원 리스트 만들어줌
    arr = [[] for _ in range(v + 1)]

    # 연결된 정점을 저장할 리스트
    krr = [0 for _ in range(v + 1)]
    for __ in range(e):
        # 인접한 두 정점의 번호를 입력 받음
        a, b = map(int, stdin.readline().split())
        # 두 인접한 정점의 번호를 각 배열에 저장
        arr[a].append(b)
        arr[b].append(a)

    # 이분 그래프인지 아닌지 판단하는 변수
    tf = True
    for i in range(1, v + 1):
        # 연결된 그룹이 없을 때 실행
        if krr[i] == 0:
            # 같은 그룹끼리 묶여있다면 False
            if not solve(i):
                tf = False
                break

    print('YES') if tf else print("NO")
