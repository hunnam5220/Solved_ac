from sys import stdin

arr = []
for x in range(4):
    n = int(stdin.readline().rstrip())
    if n > 0:
        arr.append(n)
    else:
        print('No Fish')
        exit()

if len(set(arr)) == 1 and list(set(arr))[0] == 0:
    print('No Fish')

elif len(set(arr)) == 1:
    print('Fish At Constant Depth')

else:
    std = arr[0]
    if std > arr[1]:
        std = arr[1]
        for x in range(2, len(arr)):
            if std > arr[x]:
                std = arr[x]
                continue
            else:
                print('No Fish')
                exit()

        print('Fish Diving')

    elif std < arr[1]:
        std = arr[1]
        for x in range(2, len(arr)):
            if std < arr[x]:
                std = arr[x]
                continue
            else:
                print('No Fish')
                exit()

        print('Fish Rising')

    else:
        print('No Fish')
