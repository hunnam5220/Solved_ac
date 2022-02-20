from sys import stdin

dictionary = {chr(x): 0 for x in range(97, 123)}

for _ in range(50):
    s = stdin.readline().rstrip()
    for i in range(97, 123):
        dictionary[chr(i)] += s.count(chr(i))


max_val = 0
for key, val in sorted(dictionary.items(), key=lambda x: -x[1]):
    if val >= max_val:
        print(key, end='')
        max_val = val
    else:
        break
