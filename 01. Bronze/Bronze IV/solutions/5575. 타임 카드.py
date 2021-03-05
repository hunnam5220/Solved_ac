from sys import stdin
import datetime

a = list(map(int, stdin.readline().rstrip().split()))
b = list(map(int, stdin.readline().rstrip().split()))
c = list(map(int, stdin.readline().rstrip().split()))

a_t = datetime.datetime.strptime(' '.join(list(map(str, a[3:]))), '%H %M %S')
b_t = datetime.datetime.strptime(' '.join(list(map(str, b[3:]))), '%H %M %S')
c_t = datetime.datetime.strptime(' '.join(list(map(str, c[3:]))), '%H %M %S')

a_result = a_t - datetime.timedelta(hours=a[0], minutes=a[1], seconds=a[2])
b_result = b_t - datetime.timedelta(hours=b[0], minutes=b[1], seconds=b[2])
c_result = c_t - datetime.timedelta(hours=c[0], minutes=c[1], seconds=c[2])

print(a_result.hour, a_result.minute, a_result.second)
print(b_result.hour, b_result.minute, b_result.second)
print(c_result.hour, c_result.minute, c_result.second)