from sys import stdin

t = int(stdin.readline().rstrip())

for step in range(t):
    n_box = int(stdin.readline().rstrip())
    j_box = n_box - 2

    for x in range(n_box):
        string = ''
        if 1 <= x < n_box-1:
            string = '#'
            for y in range(j_box):
                string += 'J'
            string += '#'
            print(string)

        else:
            for x in range(n_box):
                string += '#'
            print(string)
    print()