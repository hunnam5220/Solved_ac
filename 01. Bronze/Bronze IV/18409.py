from sys import stdin

m = ['i', 'u', 'e', 'o', 'a']
n = int(stdin.readline())
s = stdin.readline().rstrip()
answer = 0
for i in m:
    answer += s.count(i)
print(answer)