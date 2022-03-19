from sys import stdin

for _ in range(int(stdin.readline())):
    cnt = 0

    temp_num = list(stdin.readline().rstrip())

    while 1:
        if ['6', '1', '7', '4'] == temp_num:
            print(cnt)
            break
        else:
            num1 = sorted(temp_num, reverse=True)
            num2 = sorted(temp_num)

            n1 = int(''.join(num1))
            n2 = int(''.join(num2))

            temp_num = list(str(abs(n1 - n2)))

            if len(temp_num) < 4:
                temp = ['0'] * (4 - len(temp_num))
                temp_num = temp + temp_num

            cnt += 1