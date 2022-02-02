from sys import stdin

n, k = map(int, stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, stdin.readline().split())))

arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))
grade = {x: [] for x in range(1, 10001)}
num = 1
now = arr[0][1:]
grade[1].append(arr[0][0])

for i in range(1, n):
    score = arr[i][1:]
    if score == now:
        grade[num].append(arr[i][0])
    else:
        if len(grade[num]) > 1:
            num += len(grade[num])
        else:
            num += 1
        grade[num].append(arr[i][0])
        now = arr[i][1:]

    if k == arr[i][0]:
        break

for key, val in grade.items():
    if k in val:
        print(key)
        break