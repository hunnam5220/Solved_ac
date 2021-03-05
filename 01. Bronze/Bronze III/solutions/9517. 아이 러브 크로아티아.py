from sys import stdin

k = int(stdin.readline().rstrip())
n = int(stdin.readline().rstrip())
x = 210

for step in range(n):
    t, z = stdin.readline().rstrip().split()

    if z == 'N' or z == 'P':
        x -= int(t)

        if x <= 0:
            break

    else:
        x -= int(t)
        if x <= 0:
            break

        if k == 8:
            k = 1
        else:
            k += 1

print(k)