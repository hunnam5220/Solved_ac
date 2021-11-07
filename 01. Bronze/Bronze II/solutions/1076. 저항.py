from sys import stdin

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
values = {color[x]: x for x in range(10)}
g = {color[x]: 10 ** x for x in range(10)}

res = ''
for _ in range(2):
    data = values[stdin.readline().rstrip()]
    if res != '' and data != 0:
        res += str(data)
    else:
        res += str(data)

res = int(res)
print(res * g[stdin.readline().rstrip()])