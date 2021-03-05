from sys import stdin
import datetime as dt

h, m, s = map(int, stdin.readline().rstrip().split())

for step in range(int(stdin.readline().rstrip())):
    hms = '%02d:%02d:%02d' % (h, m, s)

    try:
        chk, c = map(int, stdin.readline().rstrip().split())
        hms_ = dt.datetime.strptime(hms, '%H:%M:%S')
        if chk == 1:
            hms_ += dt.timedelta(seconds=c)
        else:
            hms_ -= dt.timedelta(seconds=c)

        h, m, s = hms_.hour, hms_.minute, hms_.second

    except:
        print(h, m, s)