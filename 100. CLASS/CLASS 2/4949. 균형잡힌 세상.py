from sys import stdin


def check(s):
    chk = ''
    for i in s:
        if i == '(' or i == ')' or i == '[' or i == ']':
            chk += i

    if chk == '':
        return True

    status, cnt = [], 0
    for i in chk:
        if i == '(':
            status.append(')')
            cnt += 1
        elif i == '[':
            status.append(']')
            cnt += 1

        elif not status and (i == ')' or i == ']'):
            return False

        elif i != status[-1]:
            return False

        elif i == status[-1]:
            status.pop()

    return True if not status else False


while 1:
    string = stdin.readline().rstrip()
    if string == '.':
        break

    if check(string):
        print('yes')
    else:
        print('no')