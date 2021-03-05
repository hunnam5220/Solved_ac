from sys import stdin

berger = [int(stdin.readline().rstrip()) for b in range(3)]
drink = [int(stdin.readline().rstrip()) for d in range(2)]

print(min(berger)+min(drink)-50)