from sys import stdin

n = int(stdin.readline())
d = {'E': 0, 'W': 1, 'S': 2, 'N': 3}
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
visited = set()
pos = [0, 0]
visited.add(tuple(pos))

for s in stdin.readline().rstrip():
    pos[0], pos[1] = pos[0] + dx[d[s]], pos[1] + dy[d[s]]
    visited.add((pos[0], pos[1]))

print(len(visited))