from sys import stdin
import heapq

n, e = map(int, stdin.readline().split())
nodes = [[] for _ in range(n + 1)]

# 양방향 노드 간선 저장
for i in range(e):
    a, b, c = map(int, stdin.readline().split())
    nodes[a].append((b, c))
    nodes[b].append((a, c))

o, p = map(int, stdin.readline().split())


# 다익스트라 알고리즘
def solve(s):
    # 거리 계산 배열
    dist = [int(1e9) for _ in range(n + 1)]
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0

    while q:
        d, now = heapq.heappop(q)

        if dist[now] > d:
            continue

        for i in nodes[now]:
            cost = d + i[1]

            if dist[i[0]] > cost:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return dist


# 각 출발지마다의 거리 배열 반환 받기
origin = solve(1)
o_dijk = solve(o)
p_dijk = solve(p)
# 시작점(1)부터 o 까지 거리 + o 부터 p 까지의 거리 + p 부터 n 까지의 거리
# 시작점(1)부터 p 까지 거리 + p 부터 o 까지의 거리 + o 부터 n 까지의 거리
ans = min((origin[o] + o_dijk[p] + p_dijk[n]), (origin[p] + p_dijk[o] + o_dijk[n]))

if ans >= int(1e9):
    print(-1)
else:
    print(ans)


