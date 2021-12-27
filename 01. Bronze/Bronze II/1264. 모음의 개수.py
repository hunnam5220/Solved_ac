from sys import stdin



while 1:
    string = stdin.readline().rstrip().lower()
    if string == '#':
        break
    res = 0

    for s in ['a', 'e', 'i', 'o', 'u']:
        res += string.count(s)
    print(res)