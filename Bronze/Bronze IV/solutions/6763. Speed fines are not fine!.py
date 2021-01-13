from sys import stdin

max_s = int(stdin.readline().rstrip())
speed = int(stdin.readline().rstrip())
check = speed - max_s

if check <= 0:
    print('Congratulations, you are within the speed limit!')
elif 1 <= check <= 20:
    print('You are speeding and your fine is $100.')
elif 21 <= check <= 30:
    print('You are speeding and your fine is $270.')
elif 31 <= check:
    print('You are speeding and your fine is $500.')