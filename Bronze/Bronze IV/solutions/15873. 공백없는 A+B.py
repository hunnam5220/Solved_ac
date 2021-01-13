from sys import stdin

num = list(stdin.readline().rstrip())
if len(num) == 3:
    if int(num[0]+num[1]) > 10:
        print(eval(num[0] + '+' + num[1] + num[-1]))
    else:
        print(eval(num[0] + num[1] + '+' + num[-1]))
elif len(num) == 4:
    print(eval(num[0] + num[1] + '+' + num[-2] + num[-1]))
else:
    print(eval(num[0] + '+' + num[1]))