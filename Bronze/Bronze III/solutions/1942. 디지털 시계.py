from sys import stdin
import datetime as dt

for step in range(3):
    time_arr = list(stdin.readline().split())
    start_t = dt.datetime.strptime(time_arr[0], '%H:%M:%S')
    end_t = dt.datetime.strptime(time_arr[1], '%H:%M:%S')
    cnt = 0
    while True:
        str_num = int(start_t.strftime('%H%M%S'))

        if str_num % 3 == 0:
            cnt += 1

        if start_t.strftime('%H%M%S') == end_t.strftime('%H%M%S'):
            break

        start_t += dt.timedelta(seconds=1)

    print(cnt)