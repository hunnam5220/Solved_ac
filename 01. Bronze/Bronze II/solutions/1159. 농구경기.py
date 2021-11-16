from sys import stdin

players = {}
res = []
for _ in range(int(stdin.readline())):
    player = stdin.readline().rstrip()
    if player[0] not in players:
        players[player[0]] = 1
    else:
        players[player[0]] += 1

for player, count in players.items():
    if count >= 5:
        res.append(player)

if res:
    res.sort()
    print(''.join(res))
else:
    print("PREDAJA")