from sys import stdin

arr = []
chk = 1

while 1:
    s = stdin.readline().rstrip()

    if s == '=':
        break

    else:
        if chk >= 3:
            arr.append(s)
            arr = [str(int(eval(''.join(arr))))]
            chk = 2
        else:
            arr.append(s)
            chk += 1

print(arr[0])