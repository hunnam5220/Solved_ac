from sys import stdin
antenna = int(stdin.readline().rstrip())
eyes = int(stdin.readline().rstrip())

if 3 <= antenna and eyes <= 4:
    print('TroyMartian')

if antenna <= 6 and 2 <= eyes:
    print('VladSaturnian')

if antenna <= 2 and eyes <= 3:
    print('GraemeMercurian')
