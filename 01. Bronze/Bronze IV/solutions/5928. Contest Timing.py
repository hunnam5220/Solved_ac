from sys import stdin
import datetime
start = datetime.datetime.strptime('11 11 11', '%d %H %M')
end = datetime.datetime.strptime(stdin.readline().rstrip(), '%d %H %M')

if end < start:
    print(-1)
else:
    t = end - datetime.timedelta(days=11, hours=11, minutes=11)
    if end.day == 11:
        print(t.hour * 60 + t.minute)
    else:
        print(t.day * 1440 + t.hour * 60 + t.minute)