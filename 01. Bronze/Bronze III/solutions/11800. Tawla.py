from sys import stdin

name_1 = {
    1: "Yakk",
    2: "Doh",
    3: "Seh",
    4: "Ghar",
    5: "Bang",
    6: "Sheesh"
}

name_2 = {
    1: "Habb Yakk",
    2: "Dobara",
    3: "Dousa",
    4: "Dorgy",
    5: "Dabash",
    6: "Dosh"
}

for step in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().rstrip().split())

    print('Case {}:'.format(step + 1), end=' ')

    if a == b:
        print(name_2[a])
    else:
        if a + b == 11:
            print('Sheesh Beesh')
        else:
            print(name_1[max([a, b])] + ' ' + name_1[min([a, b])])