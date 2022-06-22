from sys import stdin

temp, words = [], []
length = 0
ans = ''

for i in range(5):
    data = stdin.readline().rstrip()
    length = max(length, len(data))
    temp.append(data)

for i in range(5):
    words.append(temp[i] + ' ' * (length - len(temp[i])))


for i in range(length):
    for j in range(5):
        ans += words[j][i]

ans = ans.replace(' ', '')
print(ans)