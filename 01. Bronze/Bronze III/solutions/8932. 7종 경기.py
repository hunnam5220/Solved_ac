from sys import stdin

for step in range(int(stdin.readline().rstrip())):
    arr = list(map(int, stdin.readline().rstrip().split()))
    _100mh = int(9.23076 * ((26.7 - arr[0]) ** 1.835))
    high_jump = int(1.84523 * ((arr[1] - 75) ** 1.348))
    po = int(56.0211 * ((arr[2] - 1.5) ** 1.05))
    _200mr = int(4.99087 * ((42.5 - arr[3]) ** 1.81))
    longer = int(0.188807 * ((arr[4] - 210) ** 1.41))
    throw = int(15.9803 * ((arr[5] - 3.8) ** 1.04))
    _800r = int(0.11193 * ((254 - arr[6]) ** 1.88))

    print(_100mh + high_jump + po + _200mr + longer + throw + _800r)