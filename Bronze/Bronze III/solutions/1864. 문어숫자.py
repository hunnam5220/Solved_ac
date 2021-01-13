from sys import stdin

match_dict ={
    '-': 0, '\\': 1, '(': 2,
    '@': 3, '?': 4, '>': 5,
    '&': 6, '%': 7, '/': -1
}

while True:
    string = stdin.readline().rstrip()
    result = 0

    if string == '#':
        break

    for x, y in zip(range(len(string)), reversed(range(len(string)))):
        a = match_dict[string[x]]
        result += a * (8 ** y)

    print(result)