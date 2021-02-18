from sys import stdin

arr = []
while 1:
    st = stdin.readline().rstrip()
    if st != '':
        arr.append(st)
    else:
        break

print('\n'.join(arr))