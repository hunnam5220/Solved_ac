from sys import stdin

for _ in range(int(stdin.readline())):
    univ = {}
    for n in range(int(stdin.readline())):
        name, ea = stdin.readline().rstrip().split()
        if name not in univ:
            univ[name] = int(ea)
        else:
            univ[name] += int(ea)

    ans = ['', 0]

    for key, item in univ.items():
        if item > ans[1]:
            ans = [key, item]

    print(ans[0])